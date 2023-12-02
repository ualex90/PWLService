from rest_framework import serializers

from app_payment.validators import VideoLinkValidator, MaterialsValidator
from app_pwl.models import Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class LessonCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"
        validators = [
            VideoLinkValidator('video'),
            MaterialsValidator('name', 'description', 'body')
        ]


class LessonListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('id', 'name', 'description', )
