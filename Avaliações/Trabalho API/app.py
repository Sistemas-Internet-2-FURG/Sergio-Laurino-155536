from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_cors import CORS
from datetime import date, datetime
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["JWT_SECRET_KEY"] = "chave" 
db = SQLAlchemy(app)
jwt = JWTManager(app)
CORS(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.String(10), nullable=False)
    tipo = db.Column(db.String(50), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    disponivel = db.Column(db.Boolean, default=True)

class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quarto_id = db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False)
    hospede = db.Column(db.String(80), nullable=False)
    data_checkin = db.Column(db.Date, nullable=False)
    data_checkout = db.Column(db.Date, nullable=False)

    room = db.relationship("Room", backref="reservations")

# Rota de Registro
@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    new_user = User(username=data["username"], password=data["password"])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created"}), 201

# Rota de Login
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data["username"]).first()
    if user and user.password == data["password"]:
        access_token = create_access_token(identity=user.id)
        return jsonify({"token": access_token}), 200
    return jsonify({"message": "Invalid credentials"}), 401

# Listar Quartos
@app.route("/rooms", methods=["GET"])
@jwt_required()
def get_rooms():
    rooms = Room.query.all()
    return jsonify([{
        "id": room.id, "numero": room.numero, "tipo": room.tipo,
        "preco": room.preco, "disponivel": room.disponivel
    } for room in rooms])

# Adiciona Quarto
@app.route("/rooms", methods=["POST"])
@jwt_required()
def add_room():
    data = request.get_json()
    new_room = Room(
        numero=data["numero"], tipo=data["tipo"],
        preco=data["preco"], disponivel=True
    )
    db.session.add(new_room)
    db.session.commit()
    return jsonify({"message": "Room added"}), 201

# Atualiza Disponibilidade do Quarto
@app.route("/rooms/<int:id>", methods=["PATCH"])
@jwt_required()
def update_room_availability(id):
    room = Room.query.get(id)
    if not room:
        return jsonify({"message": "Room not found"}), 404

    data = request.get_json()
    room.disponivel = data.get("disponivel", room.disponivel)
    db.session.commit()
    return jsonify({"message": "Room availability updated"}), 200

#Cria Reserva e Verifica Conflito de Datas
@app.route("/reserve", methods=["POST"])
@jwt_required()
def create_reservation():
    data = request.get_json()
    quarto_id = data.get("quarto_id")
    hospede = data.get("hospede")
    data_checkin = datetime.strptime(data.get("data_checkin"), "%Y-%m-%d").date()
    data_checkout = datetime.strptime(data.get("data_checkout"), "%Y-%m-%d").date()

    # Verificação de conflito de datas
    reservas_existentes = Reservation.query.filter_by(quarto_id=quarto_id).all()
    for reserva in reservas_existentes:
        if (data_checkin <= reserva.data_checkout and data_checkout >= reserva.data_checkin):
            return jsonify({"message": "Conflito de datas para o quarto selecionado"}), 409

    # Criar nova reserva
    nova_reserva = Reservation(
        quarto_id=quarto_id,
        hospede=hospede,
        data_checkin=data_checkin,
        data_checkout=data_checkout
    )
    db.session.add(nova_reserva)
    db.session.commit()

    return jsonify({"message": "Reserva criada com sucesso"}), 201

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
