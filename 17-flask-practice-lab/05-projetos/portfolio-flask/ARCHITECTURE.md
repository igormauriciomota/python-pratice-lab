# Arquitetura e função de cada camada

## 1. Inicialização

`run.py` importa a função `create_app()` e inicia o servidor local. `wsgi.py` expõe a mesma aplicação para Gunicorn em produção. A fábrica localizada em `app/__init__.py` cria o Flask, lê a configuração, conecta extensões e registra os Blueprints.

## 2. Banco de dados

`app/models.py` define quatro entidades:

- `User`: administrador com senha armazenada por hash.
- `Profile`: dados pessoais, links, foto e currículo.
- `Project`: título, descrição, stack, status, GitHub, vídeo e sistema online.
- `Article`: rascunhos e artigos publicados.

No desenvolvimento, `sqlite:///portfolio.db` atende bem. Em produção, basta fornecer uma URL PostgreSQL em `DATABASE_URL`.

## 3. Rotas públicas

O Blueprint `main` consulta somente registros publicados/destacados e envia objetos reais para `templates/main/index.html`. O template não contém projetos fictícios: quando o banco está vazio, explica que o conteúdo será adicionado pelo painel.

## 4. Autenticação

O Blueprint `auth` valida e-mail e senha. `check_password_hash()` compara a senha digitada com o hash salvo. `Flask-Login` grava apenas o identificador do usuário na sessão.

## 5. Administração

Todas as rotas do Blueprint `admin` usam `@login_required`. O administrador pode:

- editar perfil e links;
- anexar foto e currículo;
- criar, editar e excluir projetos;
- anexar capa e cadastrar URLs de código, vídeo e demonstração.

`app/services/storage.py` centraliza nomes seguros, extensões e gravação. Isso evita repetir regras de upload nas rotas.

## 6. Front-end

`base.html` define metadados, Bootstrap e blocos Jinja. `index.html` monta menu lateral, hero, habilidades, carrossel e contato. `app.css` implementa a identidade navy/amarelo e a responsividade. `app.js` mantém o menu sincronizado com a seção visível e controla o carrossel sem bibliotecas pesadas.

## 7. Evoluções recomendadas

- Flask-Migrate/Alembic para versionar alterações de banco.
- R2 ou S3 para uploads persistentes.
- GitHub API com cache para contribuições recentes.
- Markdown seguro para artigos.
- CI no GitHub Actions com Ruff, Pytest e cobertura.
