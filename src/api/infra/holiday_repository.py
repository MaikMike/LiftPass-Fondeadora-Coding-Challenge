from datetime import date
from database.models.holiday import Holiday


class HolidayRepository:
    def __init__(self):
        pass

    def find_by_date(self, date: date):
        return Holiday.query.filter_by(date=date).first()
