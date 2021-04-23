import pytest
from .context import api

from api.domain.age import Age
from api.domain.pass_type import PassType
from api.use_case.night_pass_price_calculator import NightPassPriceCalculator
from test.mock.price_repository import PriceRepositoryMock


def test_base_night():
    price_calculator = NightPassPriceCalculator(PriceRepositoryMock())
    age = Age(20)
    pass_type = PassType('Night')
    assert price_calculator.execute(age, pass_type) == 19


def test_child_night():
    price_calculator = NightPassPriceCalculator(PriceRepositoryMock())
    age = Age(5)
    pass_type = PassType('Night')
    assert price_calculator.execute(age, pass_type) == 0


def test_elderly_night():
    price_calculator = NightPassPriceCalculator(PriceRepositoryMock())
    age = Age(65)
    pass_type = PassType('Night')
    assert price_calculator.execute(age, pass_type) == 8

