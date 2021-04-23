from api.domain.age import Age
from api.domain.pass_type import PassType
from api.use_case.price_discount_calculator import PriceDiscountCalculator


class NightPassPriceCalculator:

    def __init__(self, price_repo):
        self.price_repo = price_repo

    def execute(self, age: Age, pass_type: PassType):
        price = self.price_repo.find_by_type(pass_type.to_primitives())
        priceCalculator = PriceDiscountCalculator()

        if age.is_child():
            return priceCalculator.execute(price.cost, [0])
        if age.is_elderly():
            return priceCalculator.execute(price.cost, [40])

        return price.cost
