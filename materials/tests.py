from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from materials.models import Course, Lesson
from users.models import User


class CourseTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="ilia.grigoriev2018@yandex.ru")
        self.course = Course.objects.create(name="курс")
        self.lesson = Lesson.objects.create(name="урок", course=self.course, owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_course_retrieve(self):
        url = reverse("materials:course-detail", args=(self.course.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.status_code, status.HTTP_200_OK
        )

    def test_course_create(self):
        url = reverse("materials:course-list")
        data = {
            "title": "course"
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(
            Course.objects.all().count(), 2
        )

    def test_course_update(self):
        url = reverse("materials:course-detail", args=(self.course.pk,))
        data = {
            "title": "course"
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.status_code, status.HTTP_200_OK
        )

    def test_course_delete(self):
        url = reverse("materials:course-detail", args=(self.course.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Course.objects.all().count(), 0
        )

    def test_course_list(self):
        url = reverse("materials:course-list")
        response = self.client.get(url)
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )


class LessonTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="ilia.grigoriev2018@yandex.ru")
        self.course = Course.objects.create(name="курс", owner=self.user)
        self.lesson = Lesson.objects.create(name="урок", course=self.course, owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        url = reverse("materials:lesson-retrieve", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.status_code, status.HTTP_200_OK
        )

    def test_lesson_update(self):
        url = reverse("materials:lesson-update", args=(self.lesson.pk,))
        data = {
            "title": "lesson1"
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.status_code, status.HTTP_200_OK
        )

    def test_lesson_delete(self):
        url = reverse("materials:lesson-delete", args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Lesson.objects.all().count(), 0
        )

    def test_lesson_list(self):
        url = reverse("materials:lesson-list")
        response = self.client.get(url)
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
