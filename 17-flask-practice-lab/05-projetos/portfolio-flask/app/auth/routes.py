from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_user, logout_user

from . import bp
from .forms import LoginForm
from ..models import User


@bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("admin.dashboard"))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data.strip().lower()).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            next_url = request.args.get("next")
            # Só aceita caminhos internos para evitar redirecionamento malicioso.
            return redirect(next_url if next_url and next_url.startswith("/") else url_for("admin.dashboard"))
        flash("E-mail ou senha inválidos.", "danger")

    return render_template("auth/login.html", form=form)


@bp.post("/logout")
def logout():
    logout_user()
    flash("Sessão encerrada.", "success")
    return redirect(url_for("main.index"))
