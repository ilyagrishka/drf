import stripe
from config.settings import STRIPE_API_KEY
from forex_python.converter import CurrencyRates

stripe.api_key = STRIPE_API_KEY


def create_product(title, description):
    try:
        product = stripe.Product.create(
            title='Название курса',
            description='Описание курса'
        )
        return product

    except Exception as e:
        return None


def convert_rub_to_dollars(sum_of_payments):
    c = CurrencyRates()
    rate = c.get_rate('RUB', 'USD')
    return int(sum_of_payments * rate)


def create_stripe_price(sum_of_payments):
    return stripe.Price.create(
        currency="usd",
        unit_amount=sum_of_payments * 100,
        product_data={"name": "Payments"},
    )


def create_stripe_session(price):
    session = stripe.checkout.Session.create(
        success_url="https://127.0.0.1:8000/",
        line_items=[{"price": price.get("id"), "quantity": 1}],
        mode="payment",
    )
    return session.get("id"), session.get("url")
