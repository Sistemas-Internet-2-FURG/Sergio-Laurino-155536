from flask import Flask, render_template, request, redirect, url_for, flash, session
from models import db, Quarto, Reserva, User
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'chave-secreta'

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

# Rotas de Autenticação
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            session['user_id'] = user.id
            flash('Login realizado com sucesso!')
            return redirect(url_for('listar_quartos'))
        flash('Usuário ou senha inválidos.')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if User.query.filter_by(username=username).first():
            flash('Usuário já existe.')
            return redirect(url_for('register'))
        new_user = User(username=username)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        flash('Usuário registrado com sucesso!')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('Logout realizado com sucesso!')
    return redirect(url_for('login'))

# Decorador para verificar login
def login_required(f):
    from functools import wraps
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Por favor, faça login para acessar esta página.')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# Rotas para Quartos
@app.route('/quartos')
@login_required
def listar_quartos():
    quartos = Quarto.query.all()
    return render_template('quartos.html', quartos=quartos)

@app.route('/quartos/add', methods=['POST'])
@login_required
def adicionar_quarto():
    numero = request.form['numero']
    tipo = request.form['tipo']
    preco = request.form['preco']

    novo_quarto = Quarto(numero=numero, tipo=tipo, preco=preco, disponivel=True)
    db.session.add(novo_quarto)
    db.session.commit()
    flash('Quarto adicionado com sucesso!')
    return redirect(url_for('listar_quartos'))

@app.route('/quartos/delete/<int:id>')
@login_required
def deletar_quarto(id):
    quarto = Quarto.query.get(id)
    db.session.delete(quarto)
    db.session.commit()
    flash('Quarto deletado com sucesso!')
    return redirect(url_for('listar_quartos'))

# Rotas para Reservas
@app.route('/reservas')
@login_required
def listar_reservas():
    reservas = Reserva.query.all()
    quartos = Quarto.query.all()
    return render_template('reservas.html', reservas=reservas, quartos=quartos)

@app.route('/reservas/add', methods=['POST'])
@login_required
def adicionar_reserva():
    hospede = request.form['hospede']
    quarto_id = request.form['quarto_id']
    data_checkin = request.form['data_checkin']
    data_checkout = request.form['data_checkout']

    quarto = Quarto.query.get(quarto_id)
    if not quarto.disponivel:
        flash('O quarto selecionado já está reservado.')
        return redirect(url_for('listar_reservas'))

    nova_reserva = Reserva(hospede=hospede, quarto_id=quarto_id, data_checkin=data_checkin, data_checkout=data_checkout)
    quarto.disponivel = False  # Marca o quarto como indisponível
    db.session.add(nova_reserva)
    db.session.commit()
    flash('Reserva adicionada com sucesso!')
    return redirect(url_for('listar_reservas'))

@app.route('/reservas/delete/<int:id>')
@login_required
def deletar_reserva(id):
    reserva = Reserva.query.get(id)
    quarto = Quarto.query.get(reserva.quarto_id)
    quarto.disponivel = True  # Marca o quarto como disponível novamente
    db.session.delete(reserva)
    db.session.commit()
    flash('Reserva deletada com sucesso e quarto liberado!')
    return redirect(url_for('listar_reservas'))

if __name__ == '__main__':
    app.run(debug=True)
