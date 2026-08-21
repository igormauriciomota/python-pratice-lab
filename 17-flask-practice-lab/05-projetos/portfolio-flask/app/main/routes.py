from flask import render_template

from . import bp
from ..extensions import db
from ..models import Article, Profile, Project
from ..services.github import recent_public_activity


@bp.get("/")
def index():
    """Consulta o banco e entrega somente conteúdo publicável ao template."""

    profile = db.session.get(Profile, 1)
    projects = (
        Project.query.filter_by(featured=True)
        .order_by(Project.sort_order.asc(), Project.id.desc())
        .all()
    )
    articles = (
        Article.query.filter_by(published=True)
        .order_by(Article.published_at.desc())
        .limit(3)
        .all()
    )
    github_activity = recent_public_activity(profile.github_url if profile else None)
    return render_template(
        "main/index.html",
        profile=profile,
        projects=projects,
        articles=articles,
        github_activity=github_activity,
    )
