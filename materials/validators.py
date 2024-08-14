from rest_framework.serializers import ValidationError

only_youtube = "youtube.com."


def validate_forbidden_links(value):
    if value.lower() not in only_youtube:
        raise ValidationError("ИСПОЛЬЗОВАНА ЗАПРЕЩЁННАЯ ССЫЛКА")
