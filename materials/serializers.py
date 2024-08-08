from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from materials.models import Course, Lesson
from materials.validators import validate_forbidden_words


class CourseSerializer(ModelSerializer):
    name = serializers.CharField(validators=[validate_forbidden_words])

    class Meta:
        model = Course
        fields = "__all__"


class CourseDetailSerializer(ModelSerializer):
    amount_of_lesson = SerializerMethodField()

    def get_amount_of_lesson(self, lesson):
        return Course.objects.filter(course=lesson.course).count()

    class Meta:
        model = Course
        fields = ("title", "description", "amount_of_lesson")


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class SubscriptionSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"
