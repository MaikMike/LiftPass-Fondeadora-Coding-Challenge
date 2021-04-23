import pytest
from .context import api

from api.domain.age import Age
from api.domain.pass_date import PassDate
from api.domain.pass_type import PassType
from api.use_case.day_pass_price_calculator import DayPassPriceCalculator
from test.mock.holiday_repository import HolidayRepositoryMock
from test.mock.price_repository import PriceRepositoryMock


def test_jour_without_discount():
    price_calculator = DayPassPriceCalculator(PriceRepositoryMock(), HolidayRepositoryMock())
    age = Age(20)
    pass_type = PassType('Jour')
    pass_date = PassDate('2020-05-08')
    assert price_calculator.execute(age, pass_type, pass_date) == 35


def test_jour_child():
    price_calculator = DayPassPriceCalculator(PriceRepositoryMock(), HolidayRepositoryMock())
    age = Age(5)
    pass_type = PassType('Jour')
    pass_date = PassDate('2020-05-08')
    assert price_calculator.execute(age, pass_type, pass_date) == 0


def test_jour_elderly():
    price_calculator = DayPassPriceCalculator(PriceRepositoryMock(), HolidayRepositoryMock())
    age = Age(65)
    pass_type = PassType('Jour')
    pass_date = PassDate('2020-05-08')
    assert price_calculator.execute(age, pass_type, pass_date) == 27


def test_holiday():
    price_calculator = DayPassPriceCalculator(PriceRepositoryMock(), HolidayRepositoryMock())
    age = Age(20)
    pass_type = PassType('Jour')
    pass_date = PassDate('2020-05-08')
    assert price_calculator.execute(age, pass_type, pass_date) == 35


def test_monday():
    price_calculator = DayPassPriceCalculator(PriceRepositoryMock(), HolidayRepositoryMock())
    age = Age(20)
    pass_type = PassType('Jour')
    pass_date = PassDate('2020-05-04')
    assert price_calculator.execute(age, pass_type, pass_date) == 23


def test_under_15yo():
    price_calculator = DayPassPriceCalculator(PriceRepositoryMock(), HolidayRepositoryMock())
    age = Age(14)
    pass_type = PassType('Jour')
    pass_date = PassDate('2020-05-04')
    assert price_calculator.execute(age, pass_type, pass_date) == 25
