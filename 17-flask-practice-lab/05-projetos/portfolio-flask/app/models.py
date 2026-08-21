from datetime import datetime, timezone

from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from .extensions import db, login_manager


def utc_now():
    return datetime.now(timezone.utc)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(180), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=utc_now, nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))


class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True, default=1)
    name = db.Column(db.String(120), nullable=False, default="Igor Mota")
    headline = db.Column(db.String(180), nullable=False)
    location = db.Column(db.String(120), nullable=False)
    bio = db.Column(db.Text, nullable=False, default="")
    email = db.Column(db.String(180))
    linkedin_url = db.Column(db.String(500))
    github_url = db.Column(db.String(500))
    photo_filename = db.Column(db.String(255))
    resume_filename = db.Column(db.String(255))
    updated_at = db.Column(db.DateTime(timezone=True), default=utc_now, onupdate=utc_now)


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(160), nullable=False)
    slug = db.Column(db.String(180), unique=True, nullable=False, index=True)
    eyebrow = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    stack = db.Column(db.String(500), nullable=False, default="")
    status = db.Column(db.String(60), nullable=False, default="Planejado")
    accent = db.Column(db.String(20), nullable=False, default="#ffd24a")
    github_url = db.Column(db.String(500))
    live_url = db.Column(db.String(500))
    video_url = db.Column(db.String(500))
    image_filename = db.Column(db.String(255))
    featured = db.Column(db.Boolean, nullable=False, default=True)
    sort_order = db.Column(db.Integer, nullable=False, default=0)
    created_at = db.Column(db.DateTime(timezone=True), default=utc_now, nullable=False)


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    slug = db.Column(db.String(220), unique=True, nullable=False, index=True)
    summary = db.Column(db.Text, nullable=False)
    body = db.Column(db.Text, nullable=False)
    published = db.Column(db.Boolean, nullable=False, default=False)
    published_at = db.Column(db.DateTime(timezone=True))
