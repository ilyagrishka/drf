from rest_framework.serializers import ModelSerializer

from users.models import User, Payments


class UserSerializers(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class PaymentsSerializers(ModelSerializer):
    class Meta:
        model = Payments
        fields = "__all__"
