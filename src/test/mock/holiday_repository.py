from datetime import datetime, date
from dataclasses import dataclass

@dataclass
class Holiday: 
    name: str
    date: date

class HolidayRepositoryMock:
    def __init__(self):
        self.data = [{'name': 'Christmas', 'date': datetime(2020, 12, 25).date()},
                     {'name': 'New Year', 'date': datetime(2021, 1, 1).date()}]

    def find_by_date(self, date: date):
        for holiday in self.data:
            if holiday['date'] == date:
                return Holiday(holiday['name'], holiday['date'])

        return None
