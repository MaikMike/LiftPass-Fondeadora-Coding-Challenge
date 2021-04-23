from flask import jsonify, request
from flask_restful import Resource

from api.domain.age import Age
from api.domain.pass_date import PassDate
from api.domain.pass_type import PassType
from api.use_case.pass_price_calculator_handler import PriceCalculatorHandler
from api.infra.price_repository import PriceRepository
from api.infra.holiday_repository import HolidayRepository


class PriceController(Resource):
    def get(self):
        args = request.args
        price_calculator = PriceCalculatorHandler(
            PriceRepository(), HolidayRepository())
        price = price_calculator.execute(
            Age(args['age']), PassDate(args['date']), PassType(args['type']))
        return jsonify({'cost': price})
