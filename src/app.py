import math
from datetime import datetime, date
from pydantic import BaseModel, Field

from flask import Flask, jsonify, request
from flask_pydantic import validate
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class Price(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(80), unique=True, nullable=False)
    cost = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Price %s: %d>' % (self.type, self.cost)


class Holiday(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return '<Holiday %s: %s>' % (self.name, self.date)


class GetPricesParam(BaseModel):
    age: int
    type: str
    date: date


@app.route('/prices')
@validate()
def prices(query: GetPricesParam):
    price = Price.query.filter_by(type=query.type).first()

    if query.age < 6:
        return jsonify({'cost': 0})

    if query.type != 'Night':
        holidays = Holiday.query.all()

        is_holiday = False
        reduction = 0

        for holiday in holidays:
            if query.date:
                date = query.date
                if date == holiday.date:
                    is_holiday = True

        if not is_holiday and query.date.weekday() == 0:
            reduction = 35

        if query.age < 15:
            return jsonify({'cost': math.ceil(price.cost * 0.7)})
        else:
            if not query.age:
                cost = price.cost * (1 - reduction / 100)
                return jsonify({'cost': math.ceil(cost)})
            else:
                if query.age > 64:
                    cost = price.cost * 0.75 * (1 - reduction / 100)
                    return jsonify({'cost': math.ceil(cost)})
                else:
                    cost = price.cost * (1 - reduction / 100)
                    return jsonify({'cost': math.ceil(cost)})
    else:
        if query.age >= 6:
            if query.age > 64:
                return jsonify({'cost': math.ceil(price.cost * 0.4)})
            else:
                return jsonify({'cost': price.cost})
        else:
            return jsonify({'cost': 0})
