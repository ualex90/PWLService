from rest_framework import serializers
from rest_framework.fields import IntegerField

from app_pwl.models import Course


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = IntegerField()

    class Meta:
        model = Course
        fields = '__all__'
