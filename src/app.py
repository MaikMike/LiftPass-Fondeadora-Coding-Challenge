import math
from datetime import datetime

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
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


@app.route('/prices')
def prices():
    price = Price.query.filter_by(type=request.args.get('type')).first()

    if int(request.args.get('age')) < 6:
        return jsonify({'cost': 0})
    else:
        if request.args.get('type') != 'Night':
            holidays = Holiday.query.all()

            is_holiday = False
            reduction = 0

            for holiday in holidays:
                if request.args.get('date'):
                    date = datetime.strptime(
                        request.args.get('date'), '%Y-%m-%d').date()
                    if date == holiday.date:
                        is_holiday = True

            if not is_holiday and datetime.strptime(request.args.get('date'), '%Y-%m-%d').weekday() == 0:
                reduction = 35

            if int(request.args.get('age')) < 15:
                return jsonify({'cost': math.ceil(price.cost * 0.7)})
            else:
                if not request.args.get('age'):
                    cost = price.cost * (1 - reduction / 100)
                    return jsonify({'cost': math.ceil(cost)})
                else:
                    if int(request.args.get('age')) > 64:
                        cost = price.cost * 0.75 * (1 - reduction / 100)
                        return jsonify({'cost': math.ceil(cost)})
                    else:
                        cost = price.cost * (1 - reduction / 100)
                        return jsonify({'cost': math.ceil(cost)})
        else:
            if int(request.args.get('age')) >= 6:
                if int(request.args.get('age')) > 64:
                    print(price.cost)
                    return jsonify({'cost': math.ceil(price.cost * 0.4)})
                else:
                    return jsonify({'cost': price.cost})
            else:
                return jsonify({'cost': 0})
