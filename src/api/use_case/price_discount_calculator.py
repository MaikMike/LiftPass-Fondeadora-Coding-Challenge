import functools
import math
from typing import List


class PriceDiscountCalculator:
    def __init__(self):
        pass

    def execute(self, price_base: int, tariffs: List[int]):
        def normalize_tariff(tarrif: int):
            return tarrif / 100.0

        return math.ceil(price_base * functools.reduce(lambda x, y: x * y, map(normalize_tariff, tariffs)))
