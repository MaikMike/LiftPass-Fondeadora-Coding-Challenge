from dataclasses import dataclass

@dataclass
class Price:
    type: str
    cost: int

class PriceRepositoryMock:
    def __init__(self):
        self.data = [{'type': 'Jour', 'cost': 35},
                     {'type': 'Night', 'cost': 19}]

    def find_by_type(self, pass_type):
        for price in self.data:
            if price['type'] == pass_type:
                return Price(price['type'], price['cost'])

        return None
