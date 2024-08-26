Gerenciamento de Reservas de Hotel

Este projeto foi desenvolvido para a gestão de reservas de um hotel, permitindo a criação, leitura, atualização e exclusão (CRUD) de quartos e reservas. A aplicação foi construída utilizando Flask, HTML/CSS, JavaScript e SQLite como banco de dados.

Arquitetura:

hotel_reservas/
│
├── app.py                    # Script principal que configura o Flask e define as rotas
├── models.py                 # Definição dos modelos (Quarto e Reserva) utilizando SQLAlchemy
├── static/                   # Diretório para arquivos estáticos
│   ├── css/
│   │   └── style.css         # Arquivo CSS para estilização das páginas
├── templates/                # Diretório para templates HTML
│   ├── base.html             # Template base para todas as páginas
│   ├── quartos.html          # Template para a página de gerenciamento de quartos
│   └── reservas.html         # Template para a página de gerenciamento de reservas
└── database.db               # Arquivo do banco de dados SQLite

Funcionalidades:

✔️ Listagem de Quartos: Permite visualizar todos os quartos cadastrados no hotel.

✔️ Adição de Quartos: Adiciona novos quartos com informações como número, tipo e preço.

✔️ Remoção de Quartos: Remove quartos existentes do sistema.

✔️ Listagem de Reservas: Visualiza todas as reservas feitas, incluindo detalhes do hóspede e do quarto.

✔️ Adição de Reservas: Cria novas reservas selecionando o quarto, o hóspede e as datas de check-in e check-out.

✔️ Remoção de Reservas: Cancela reservas existentes.


Uso:

pip install Flask

Inicialize o banco de dados executando o seguinte comando:

>>> from app import db
>>> db.create_all()
>>> exit()

Execute a aplicação com o comando:

>>> python app.py

Acesse a aplicação no seu navegador através do endereço http://localhost:5000.
