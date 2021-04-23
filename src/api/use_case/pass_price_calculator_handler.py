from api.domain.age import Age
from api.domain.pass_date import PassDate
from api.domain.pass_type import PassType
from api.use_case.day_pass_price_calculator import DayPassPriceCalculator
from api.use_case.night_pass_price_calculator import NightPassPriceCalculator


class PriceCalculatorHandler:
    def __init__(self, price_repo, holiday_repo):
        self.price_repo = price_repo
        self.holiday_repo = holiday_repo

    def execute(self, age: Age, pass_date: PassDate, pass_type: PassType):
        if pass_type.is_day_pass():
            price_calculator = DayPassPriceCalculator(
                self.price_repo, self.holiday_repo)
            return price_calculator.execute(age, pass_type, pass_date)
        elif pass_type.is_night_pass():
            price_calculator = NightPassPriceCalculator(self.price_repo)
            return price_calculator.execute(age, pass_type)
