**API de Gerenciamento de Reservas de Hotel**

Esta API foi desenvolvida para gerenciar reservas de quartos de um hotel, permitindo a visualização, criação e gerenciamento de reservas com autenticação segura por JWT. A API é construída com Flask e possui um frontend em HTML e JavaScript para interação.

**Estrutura do Projeto**

projeto/
├── app.py               # Arquivo principal da aplicação Flask
├── models.py            # Definição dos modelos de dados (User, Room, Reservation)
├── static/              # Arquivos estáticos (CSS, JS)
│   └── css/style.css    # Arquivo de estilo para o frontend
├── templates/           # Páginas HTML
│   ├── login.html       # Página de login
│   ├── quartos.html     # Página de listagem e reserva de quartos
│   └── reservas.html    # Página de reservas ativas
└── database.db          # Banco de dados SQLite

**Tecnologias Utilizadas**

    Flask para o backend
    SQLite como banco de dados
    Flask-JWT-Extended para autenticação com JWT
    Flask-CORS para permitir o acesso ao frontend
    HTML e JavaScript para o frontend

**Configuração**

Instale as dependências:

pip install flask flask_sqlalchemy flask_jwt_extended flask_cors

Configure o banco de dados: Execute o código para criar o banco de dados e as tabelas:

python app.py

Inicie o servidor:

    python app.py

    O servidor estará disponível em http://127.0.0.1:5000.

**Endpoints**

**Autenticação**

    POST /register: Registra um novo usuário.
        Parâmetros: username, password
        Resposta: {"message": "User created"}
    POST /login: Autentica o usuário e retorna um token JWT.
        Parâmetros: username, password
        Resposta: {"token": "<jwt_token>"}

**Gestão de Quartos**

    GET /rooms: Lista todos os quartos disponíveis.
        Requer Autenticação: Sim
        Resposta: Lista de quartos com detalhes (ex.: número, tipo, preço, disponibilidade)
    POST/rooms: Inclui um quarto.
        Requer Autenticação: Sim
        Resposta: {"message": "Room added"}
        
**Gerenciamento de Reservas**

    POST /reserve: Cria uma reserva para um quarto específico.
        Requer Autenticação: Sim
        Parâmetros: hospede, quarto_id, data_checkin, data_checkout
        Resposta: {"message": "Reserva criada com sucesso"} ou {"message": "Conflito de datas para o quarto selecionado"}

**Como Usar**
Login e Token JWT

    Faça uma requisição POST /login com o username e password.
    Armazene o token JWT retornado para autenticação nos demais endpoints.

**Listar Quartos Disponíveis**

    Envie uma requisição GET /rooms com o token JWT no cabeçalho Authorization: Bearer <token>.
    A API retornará a lista de quartos disponíveis.

**Criar uma Reserva**

    Envie uma requisição POST /reserve com os detalhes da reserva (nome do hóspede, ID do quarto, data de check-in e data de check-out).
    Certifique-se de que o token JWT esteja incluído no cabeçalho de autorização.
