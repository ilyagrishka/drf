from django.utils.decorators import method_decorator
from django_filters.rest_framework import filters, DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema

from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, \
    get_object_or_404
from materials.models import Course, Lesson
from materials.paginations import CustomPagination
from materials.serializers import CourseSerializer, LessonSerializer, CourseDetailSerializer, SubscriptionSerializer

from users.permissins import IsOwner, IsModer


@method_decorator(name='list', decorator=swagger_auto_schema(
    operation_description="description from swagger_auto_schema via method_decorator"
))
class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ('course', 'lesson', " payment_method")
    ordering_fields = ("payments_day",)
    pagination_class = CustomPagination

    def get_serializer_class(self):
        if self.action == "retrieve":
            return CourseDetailSerializer
        return CourseSerializer

    def get_permissions(self):
        if self.action in "create":
            self.permission_classes = (~IsModer,)
        elif self.action in ["update", "retrieve"]:
            self.permission_classes = (IsModer | IsOwner,)
        elif self.action == "destroy":
            self.permission_classes = (~IsModer, IsOwner)
        return super().get_permissions()


class LessonCreateApiView(CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (~IsModer, IsAuthenticated)


class LessonListApiView(ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    pagination_class = CustomPagination


class LessonRetrieveApiView(RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsModer, IsAuthenticated | IsOwner)


class LessonUpdateApiView(UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsModer, IsAuthenticated | IsOwner)

    @action(detail=True, methods=("post",))
    def update_course(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        if course.update_course(pk=request.user.pk).exists():
            course.update_course.send_mail(course.owner.email)
        serializer = self.get_serializer(course)
        return  Response(data=serializer.data)


class LessonDestroyApiView(DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated, IsOwner | ~IsModer)


class SubscriptionCreateApiView(CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = (~IsModer, IsAuthenticated)


class SubscriptionListApiView(ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = SubscriptionSerializer
    pagination_class = CustomPagination


class SubscriptionRetrieveApiView(RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = (IsModer, IsAuthenticated | IsOwner)


class SubscriptionUpdateApiView(UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = (IsModer, IsAuthenticated | IsOwner)


class SubscriptionDestroyApiView(DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = (IsAuthenticated, IsOwner | ~IsModer)
