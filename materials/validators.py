from rest_framework.serializers import ValidationError

forbidden_words = ["ставки", "крипта", "казино"]


def validate_forbidden_words(value):
    if value.lower() in forbidden_words:
        raise ValidationError("ИСПОЛЬЗОВАНО ЗАПРЕЩЁННОЕ СЛОВО")
