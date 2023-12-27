from rest_framework import serializers
from .models import Lesson, Group


class GroupDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('name', 'short_name', 'lessons')