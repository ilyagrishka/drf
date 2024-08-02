from django.db import models


class Course(models.Model):
    title = models.CharField(
        max_length=150,
        verbose_name="название курса")

    photo = models.ImageField(
        upload_to="materials/photo",
        verbose_name="Фото",
        help_text="Загрузите новое фото",
    )

    description = models.TextField(
        max_length=200,
        verbose_name="описание"
    )


class Lesson(models.Model):
    title = models.CharField(
        max_length=150,
        verbose_name="название курса")

    description = models.TextField(
        max_length=200,
        verbose_name="описание"
    )

    photo = models.ImageField(
        upload_to="materials/photo",
        verbose_name="Фото",
        help_text="Загрузите новое фото",
    )

    course = models.ForeignKey(Course,
                               on_delete=models.SET_NULL,
                               verbose_name="курс",
                               blank=True,
                               null=True,
                               )
