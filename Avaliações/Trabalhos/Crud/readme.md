Gerenciamento de Reservas de Hotel

Este projeto foi desenvolvido para a gestão de reservas de um hotel, permitindo a criação, leitura, atualização e exclusão (CRUD) de quartos e reservas. A aplicação foi construída utilizando Flask, HTML/CSS, JavaScript e SQLite como banco de dados.

Arquitetura:

hotel_reservas/
│
├── app.py                    # Script principal que configura o Flask, define as rotas e implementa a autenticação
├── models.py                 # Definição dos modelos (User, Quarto e Reserva) utilizando SQLAlchemy
├── static/                   # Diretório para arquivos estáticos
│   ├── css/
│   │   └── style.css         # Arquivo CSS para estilização das páginas
│   └── js/
│       └── script.js         # Arquivo JS opcional para melhorar a experiência do usuário
├── templates/                # Diretório para templates HTML
│   ├── base.html             # Template base para todas as páginas
│   ├── login.html            # Template para a página de login
│   ├── register.html         # Template para a página de registro
│   ├── quartos.html          # Template para a página de gerenciamento de quartos
│   └── reservas.html         # Template para a página de gerenciamento de reservas
└── database.db               # Arquivo do banco de dados SQLite (gerado automaticamente)


Funcionalidades:

✔️ Login de Usuário: Autenticação de usuários registrados.

✔️ Registro de Usuário: Permite que novos usuários se cadastrem.

✔️ Logout de Usuário: Desconecta o usuário da sessão ativa.

✔️ Listagem de Quartos: Visualize todos os quartos cadastrados no hotel, incluindo sua disponibilidade.

✔️ Adição de Quartos: Adicione novos quartos com informações como número, tipo e preço.

✔️ Remoção de Quartos: Remova quartos existentes do sistema.

✔️ Listagem de Reservas: Visualize todas as reservas feitas, incluindo detalhes do hóspede, datas e quarto reservado.

✔️ Adição de Reservas: Crie novas reservas selecionando o quarto, o hóspede e as datas de check-in e check-out, com verificação de disponibilidade do quarto.

✔️ Remoção de Reservas: Cancele reservas existentes, liberando automaticamente o quarto para novas reservas.


Uso:

pip install Flask

Inicialize o banco de dados executando o seguinte comando:

>>> from app import db
>>> db.create_all()
>>> exit()

Execute a aplicação com o comando:

>>> python app.py

Acesse a aplicação no seu navegador através do endereço http://localhost:5000.
