from django.urls import path
from rest_framework.routers import SimpleRouter
from materials.views import CourseViewSet
from materials.apps import MaterialsConfig
from materials.views import LessonListApiView, LessonCreateApiView, LessonUpdateApiView, LessonDestroyApiView, \
    LessonRetrieveApiView

app_name = MaterialsConfig

router = SimpleRouter()
router.register("", CourseViewSet)

urlpatterns = [
    path("lessons/", LessonListApiView.as_view()),
    path("lessons/<int:pk>", LessonRetrieveApiView.as_view()),
    path("lessons/create/", LessonCreateApiView.as_view()),
    path("lessons/<int:pk>/delete/", LessonDestroyApiView.as_view()),
    path("lessons/<int:pk>/update/", LessonUpdateApiView.as_view())
]

urlpatterns += router.urls
