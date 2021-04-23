from datetime import date
from database.models.price import Price


class PriceRepository:
    def __init__(self):
        pass

    def find_by_type(self, type: str):
        return Price.query.filter_by(type=type).first()
