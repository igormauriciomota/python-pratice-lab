# Igor Mota — Portfólio Flask Profissional

Portfólio modular em Python/Flask para apresentar projetos, vídeos, links de demonstração, artigos, currículo e contato. O conteúdo público é gerenciado por uma área administrativa e armazenado no banco SQLite.

## O que o projeto demonstra

- Application Factory e Blueprints para separar responsabilidades.
- SQLAlchemy para persistência de usuários, perfil, projetos e artigos.
- Flask-Login para sessão administrativa.
- Flask-WTF/CSRF para proteger formulários.
- Upload validado de foto, currículo PDF e capas de projetos.
- Slugs, links para GitHub, demonstração em nuvem e vídeo.
- Bootstrap 5, CSS responsivo e JavaScript leve.
- Testes básicos de rotas com Pytest.

## Início rápido

```bash
python -m venv venv
# Windows
venv\Scripts\activate

pip install -r requirements.txt
copy .env.example .env
python seed.py
python run.py
```

Acesse `http://127.0.0.1:5000`. O comando `seed.py` solicita o primeiro usuário administrador sem gravar senha no código-fonte.

## Estrutura

```text
flask-source/
├── app/
│   ├── admin/          # CRUD do conteúdo
│   ├── auth/           # login e logout
│   ├── main/           # páginas públicas
│   ├── static/         # CSS, JavaScript e uploads locais
│   ├── templates/      # Jinja + Bootstrap
│   ├── __init__.py     # Application Factory
│   ├── extensions.py   # extensões sem acoplamento circular
│   └── models.py       # tabelas SQLAlchemy
├── tests/
├── config.py
├── run.py
├── seed.py
└── wsgi.py
```

Leia também [ARCHITECTURE.md](ARCHITECTURE.md) para entender o fluxo arquivo por arquivo.

## Antes de publicar

1. Troque `SECRET_KEY` e `ADMIN_EMAIL` no ambiente.
2. Cadastre e-mail, LinkedIn, GitHub e currículo pelo painel.
3. Troque SQLite por PostgreSQL definindo `DATABASE_URL` na nuvem.
4. Armazene uploads em serviço de objetos (S3/R2) para ambientes efêmeros.
5. Execute `pytest` e desative o modo debug.
