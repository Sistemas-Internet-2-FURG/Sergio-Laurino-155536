from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Quarto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.String(50), nullable=False)
    tipo = db.Column(db.String(50), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    reservas = db.relationship('Reserva', backref='quarto', lazy=True)

class Reserva(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hospede = db.Column(db.String(100), nullable=False)
    quarto_id = db.Column(db.Integer, db.ForeignKey('quarto.id'), nullable=False)
    data_checkin = db.Column(db.String(50), nullable=False)
    data_checkout = db.Column(db.String(50), nullable=False)
