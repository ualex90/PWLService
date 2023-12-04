from rest_framework import serializers

from app_payment.models import StripeSession


class StripeSessionSerializer(serializers.ModelSerializer):

    class Meta:
        model = StripeSession
        fields = '__all__'

