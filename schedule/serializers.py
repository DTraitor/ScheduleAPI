from rest_framework import serializers
from .models import Lesson, Group


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name', 'short_name')


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('id', 'name', 'short_name', 'description', 'teacher', 'link',
                  'location', 'type', 'repeat_type', 'repeat_interval')
