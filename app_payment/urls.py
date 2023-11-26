from django.urls import path

from app_payment.views import PaymentListAPIView

urlpatterns = [
    path('', PaymentListAPIView.as_view()),
]
