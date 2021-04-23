from api.domain.age import Age
from api.domain.pass_date import PassDate
from api.domain.pass_type import PassType
from api.use_case.price_discount_calculator import PriceDiscountCalculator


class DayPassPriceCalculator:

    def __init__(self, price_repo, holiday_repo):
        self.price_repo = price_repo
        self.holiday_repo = holiday_repo

    def execute(self, age: Age, pass_type: PassType, pass_date: PassDate):
        price = self.price_repo.find_by_type(pass_type.to_primitives())
        price_calculator = PriceDiscountCalculator()
        date_tarrif = self.__compute_date_tariff(pass_date)

        if age.is_child():
            return price_calculator.execute(price.cost, [0])
        if age.is_under_15():
            return price_calculator.execute(price.cost, [70])
        if age.is_elderly():
            return price_calculator.execute(price.cost, [75, date_tarrif])

        return price_calculator.execute(price.cost, [date_tarrif])

    def __compute_date_tariff(self, pass_date: PassDate):
        holiday_date = self.holiday_repo.find_by_date(pass_date.to_primitives())

        if holiday_date and pass_date.is_monday_pass():
            return 100

        if pass_date.is_monday_pass():
            return 65

        return 100
