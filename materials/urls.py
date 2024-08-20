from django.urls import path
from rest_framework.routers import SimpleRouter
from materials.views import CourseViewSet, SubscriptionUpdateApiView, SubscriptionDestroyApiView, \
    SubscriptionCreateApiView, SubscriptionRetrieveApiView, SubscriptionListApiView
from materials.apps import MaterialsConfig
from materials.views import LessonListApiView, LessonCreateApiView, LessonUpdateApiView, LessonDestroyApiView, \
    LessonRetrieveApiView

app_name = MaterialsConfig.name

router = SimpleRouter()
router.register("", CourseViewSet)

urlpatterns = [
    path("lessons/", LessonListApiView.as_view()),
    path("lessons/<int:pk>", LessonRetrieveApiView.as_view()),
    path("lessons/create/", LessonCreateApiView.as_view()),
    path("lessons/<int:pk>/delete/", LessonDestroyApiView.as_view()),
    path("lessons/<int:pk>/update/", LessonUpdateApiView.as_view()),

    path("subscriptions/", SubscriptionListApiView.as_view()),
    path("subscription/<int:pk>", SubscriptionRetrieveApiView.as_view()),
    path("subscription/create/", SubscriptionCreateApiView.as_view()),
    path("subscription/<int:pk>/delete/", SubscriptionDestroyApiView.as_view()),
    path("subscription/<int:pk>/update/", SubscriptionUpdateApiView.as_view())

]

urlpatterns += router.urls
