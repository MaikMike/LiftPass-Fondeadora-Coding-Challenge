from datetime import datetime

from src.app import db, Price, Holiday

db.create_all()

jour = Price(type='Jour', cost=35)
night = Price(type='Night', cost=19)

christmas = Holiday(name='Christmas', date=datetime(2020, 12, 25).date())
new_year = Holiday(name='New Year', date=datetime(2021, 1, 1).date())

db.session.add(jour)
db.session.add(night)
db.session.add(christmas)
db.session.add(new_year)
db.session.commit()
