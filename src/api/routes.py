from api.infra.price_controller import PriceController


def initialize_routes(api):
    api.add_resource(PriceController, '/prices')
