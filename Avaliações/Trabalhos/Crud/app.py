from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Quarto, Reserva

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'chave-secreta'

db.init_app(app)

# Cria as tabelas se não existirem
with app.app_context():
    db.create_all()

# Rotas para Quartos
@app.route('/quartos')
def listar_quartos():
    quartos = Quarto.query.all()
    return render_template('quartos.html', quartos=quartos)

@app.route('/quartos/add', methods=['POST'])
def adicionar_quarto():
    numero = request.form['numero']
    tipo = request.form['tipo']
    preco = request.form['preco']

    novo_quarto = Quarto(numero=numero, tipo=tipo, preco=preco)
    db.session.add(novo_quarto)
    db.session.commit()
    flash('Quarto adicionado com sucesso!')
    return redirect(url_for('listar_quartos'))

@app.route('/quartos/delete/<int:id>')
def deletar_quarto(id):
    quarto = Quarto.query.get(id)
    db.session.delete(quarto)
    db.session.commit()
    flash('Quarto deletado com sucesso!')
    return redirect(url_for('listar_quartos'))

# Rotas para Reservas
@app.route('/reservas')
def listar_reservas():
    reservas = Reserva.query.all()
    quartos = Quarto.query.all()
    return render_template('reservas.html', reservas=reservas, quartos=quartos)

@app.route('/reservas/add', methods=['POST'])
def adicionar_reserva():
    hospede = request.form['hospede']
    quarto_id = request.form['quarto_id']
    data_checkin = request.form['data_checkin']
    data_checkout = request.form['data_checkout']

    nova_reserva = Reserva(hospede=hospede, quarto_id=quarto_id, data_checkin=data_checkin, data_checkout=data_checkout)
    db.session.add(nova_reserva)
    db.session.commit()
    flash('Reserva adicionada com sucesso!')
    return redirect(url_for('listar_reservas'))

@app.route('/reservas/delete/<int:id>')
def deletar_reserva(id):
    reserva = Reserva.query.get(id)
    db.session.delete(reserva)
    db.session.commit()
    flash('Reserva deletada com sucesso!')
    return redirect(url_for('listar_reservas'))

if __name__ == '__main__':
    app.run(debug=True)
