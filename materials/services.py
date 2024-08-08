import stripe
from config.settings import STRIPE_API_KEY
from forex_python.converter import CurrencyRates

stripe.api_key = STRIPE_API_KEY


def convert_rub_to_dollars(sum_of_payments):
    c = CurrencyRates()
    rate = c.get_rate('RUB', 'USD')
    return int(sum_of_payments * rate)


def create_stripe_price(sum_of_payments):
    stripe.Price.create(
        currency="usd",
        unit_amount=sum_of_payments * 100,
        product_data={"name": "Payments"},
    )
