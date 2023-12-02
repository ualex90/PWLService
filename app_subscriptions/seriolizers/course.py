from rest_framework import serializers

from app_subscriptions.models import Subscribe


class CourseSubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribe
        fields = '__all__'
