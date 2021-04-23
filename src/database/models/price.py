from ..db import db


class Price(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(80), unique=True, nullable=False)
    cost = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Price %s: %d>' % (self.type, self.cost)
