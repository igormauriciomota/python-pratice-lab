import re
import unicodedata

from flask import flash, redirect, render_template, url_for
from flask_login import login_required

from . import bp
from .forms import ProfileForm, ProjectForm
from ..extensions import db
from ..models import Profile, Project
from ..services.storage import DOCUMENT_EXTENSIONS, IMAGE_EXTENSIONS, save_upload


def slugify(value):
    normalized = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    return re.sub(r"[^a-z0-9]+", "-", normalized.lower()).strip("-")


@bp.get("/")
@login_required
def dashboard():
    projects = Project.query.order_by(Project.sort_order.asc(), Project.id.desc()).all()
    return render_template("admin/dashboard.html", projects=projects)


@bp.route("/perfil", methods=["GET", "POST"])
@login_required
def profile_edit():
    profile = db.session.get(Profile, 1) or Profile(id=1, headline="Desenvolvedor Python & Analista de Dados", location="Belo Horizonte, MG")
    form = ProfileForm(obj=profile)
    if form.validate_on_submit():
        form.populate_obj(profile)
        try:
            photo = save_upload(form.photo.data, "profile", IMAGE_EXTENSIONS)
            resume = save_upload(form.resume.data, "resume", DOCUMENT_EXTENSIONS)
        except ValueError as error:
            flash(str(error), "danger")
            return render_template("admin/profile_form.html", form=form, profile=profile)

        if photo:
            profile.photo_filename = photo
        if resume:
            profile.resume_filename = resume
        db.session.add(profile)
        db.session.commit()
        flash("Perfil atualizado.", "success")
        return redirect(url_for("admin.dashboard"))
    return render_template("admin/profile_form.html", form=form, profile=profile)


@bp.route("/projetos/novo", methods=["GET", "POST"])
@login_required
def project_create():
    form = ProjectForm()
    if form.validate_on_submit():
        project = Project()
        form.populate_obj(project)
        project.slug = unique_slug(form.title.data)
        try:
            project.image_filename = save_upload(form.image.data, "projects", IMAGE_EXTENSIONS)
        except ValueError as error:
            flash(str(error), "danger")
            return render_template("admin/project_form.html", form=form, title="Novo projeto")
        db.session.add(project)
        db.session.commit()
        flash("Projeto publicado.", "success")
        return redirect(url_for("admin.dashboard"))
    return render_template("admin/project_form.html", form=form, title="Novo projeto")


@bp.route("/projetos/<int:project_id>/editar", methods=["GET", "POST"])
@login_required
def project_edit(project_id):
    project = db.get_or_404(Project, project_id)
    form = ProjectForm(obj=project)
    if form.validate_on_submit():
        form.populate_obj(project)
        project.slug = unique_slug(form.title.data, project.id)
        try:
            image = save_upload(form.image.data, "projects", IMAGE_EXTENSIONS)
        except ValueError as error:
            flash(str(error), "danger")
            return render_template("admin/project_form.html", form=form, title="Editar projeto")
        if image:
            project.image_filename = image
        db.session.commit()
        flash("Projeto atualizado.", "success")
        return redirect(url_for("admin.dashboard"))
    return render_template("admin/project_form.html", form=form, title="Editar projeto")


@bp.post("/projetos/<int:project_id>/excluir")
@login_required
def project_delete(project_id):
    project = db.get_or_404(Project, project_id)
    db.session.delete(project)
    db.session.commit()
    flash("Projeto excluído.", "success")
    return redirect(url_for("admin.dashboard"))


def unique_slug(title, current_id=None):
    base = slugify(title) or "projeto"
    candidate = base
    counter = 2
    while True:
        query = Project.query.filter_by(slug=candidate)
        if current_id:
            query = query.filter(Project.id != current_id)
        if not query.first():
            return candidate
        candidate = f"{base}-{counter}"
        counter += 1
