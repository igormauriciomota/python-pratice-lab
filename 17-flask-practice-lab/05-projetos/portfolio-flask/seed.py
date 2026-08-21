from getpass import getpass

from app import create_app
from app.extensions import db
from app.models import Profile, User


app = create_app()

with app.app_context():
    email = input("E-mail do administrador: ").strip().lower()
    password = getpass("Senha forte: ")

    if User.query.filter_by(email=email).first():
        raise SystemExit("Este administrador já existe.")

    user = User(email=email)
    user.set_password(password)
    db.session.add(user)

    if not db.session.get(Profile, 1):
        db.session.add(
            Profile(
                id=1,
                name="Igor Mota",
                headline="Desenvolvedor Python & Analista de Dados",
                location="Belo Horizonte, MG",
                bio="Tecnologia aplicada a controladoria, dados e processos empresariais.",
            )
        )

    db.session.commit()
    print("Administrador e perfil inicial criados.")
