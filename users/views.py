from django.shortcuts import render

from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from users.services import convert_rub_to_dollars, create_stripe_price, create_stripe_session, create_product
from users.serializers import PaymentsSerializers, UserSerializers

from users.models import User, Payments



class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializers
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class PaymentsCreateAPIView(CreateAPIView):
    serializer_class = PaymentsSerializers
    queryset = Payments.objects.all()

    def perform_create(self, serializer):
        payment = serializer.save(user=self.request.user)
        amount_in_dollars = convert_rub_to_dollars(payment.sum_of_payments)
        product = create_product(
            title=lesson.title,
            description= lesson.description
        )
        price = create_stripe_price(product)
        session_id, payment_link = create_stripe_session(price)
        payment.session_id = session_id
        payment_link = payment_link
        payment.save()
