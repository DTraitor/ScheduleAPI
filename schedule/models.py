import uuid
from django.db import models


class Lesson(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    # Lesson name
    name = models.CharField(max_length=30)
    # Lesson short name
    short_name = models.CharField(max_length=10)
    # Lesson description
    description = models.TextField(max_length=200)
    # Lesson teacher
    teacher = models.CharField(max_length=30)
    # Lesson link
    link = models.URLField(null=True)
    # Lesson location
    location = models.CharField(max_length=30, null=True)
    # Lesson start time
    start_time = models.DateField()
    # Lesson end time
    end_time = models.DateField()

    class LessonType(models.IntegerChoices):
        LECTURE = 0, 'Lecture'
        PRACTICE = 1, 'Practice'
        LAB = 2, 'Lab'
        SEMINAR = 3, 'Seminar'
        EXAM = 4, 'Exam'
        OTHER = 5, 'Other'

    # Lesson type (e.g. "Lecture")
    kind = models.PositiveIntegerField(choices=LessonType.choices)

    class RepeatType(models.IntegerChoices):
        EVERY_YEAR = 0, 'Every year'
        EVERY_MONTH = 1, 'Every month'
        EVERY_WEEK = 2, 'Every week'
        EVERY_DAY = 3, 'Every day'

    # Repeat type (e.g. "Every week")
    repeat_type = models.PositiveIntegerField(choices=RepeatType.choices)
    # Repeat interval (e.g. "1")
    repeat_interval = models.PositiveIntegerField()


class Group(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    # Faculty abbreviation + group number (e.g. "FCSE 224")
    name = models.CharField(max_length=30)
    # Group name (e.g. "SE-224B")
    short_name = models.CharField(max_length=10)
    # List of lessons for this group
    lessons = models.ManyToManyField(Lesson)
