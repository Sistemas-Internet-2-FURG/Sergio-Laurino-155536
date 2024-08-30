from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Quarto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.String(50), nullable=False)
    tipo = db.Column(db.String(50), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    disponivel = db.Column(db.Boolean, default=True)  # Campo para verificar disponibilidade
    reservas = db.relationship('Reserva', backref='quarto', lazy=True)

class Reserva(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hospede = db.Column(db.String(100), nullable=False)
    quarto_id = db.Column(db.Integer, db.ForeignKey('quarto.id'), nullable=False)
    data_checkin = db.Column(db.String(50), nullable=False)
    data_checkout = db.Column(db.String(50), nullable=False)
