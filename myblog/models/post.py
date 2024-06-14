from datetime import datetime
from myblog import db

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(100))
    body = db.Column(db.Text)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    author = db.relationship('User', backref=db.backref('posts', lazy=True))

    def __init__(self, author_id, title, body) -> None:
        self.author_id = author_id
        self.title = title
        self.body = body

    def __repr__(self) -> str:
        return f'Post: {self.title}'
