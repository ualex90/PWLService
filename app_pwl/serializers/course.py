from rest_framework import serializers
from rest_framework.fields import IntegerField, ListField, SerializerMethodField

from app_pwl.models import Course, Lesson
from app_pwl.serializers.lesson import LessonListSerializer


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'


class CourseListSerializer(serializers.ModelSerializer):
    lesson_count = IntegerField()  # Поле определяется в queryset во view

    class Meta:
        model = Course
        fields = '__all__'


class CourseRetrieveSerializer(serializers.ModelSerializer):
    lessons = LessonListSerializer(many=True)

    class Meta:
        model = Course
        fields = '__all__'
