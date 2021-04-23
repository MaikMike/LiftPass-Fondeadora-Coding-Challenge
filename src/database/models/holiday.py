from ..db import db


class Holiday(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return '<Holiday %s: %s>' % (self.name, self.date)
