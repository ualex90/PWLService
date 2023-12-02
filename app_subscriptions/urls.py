from django.urls import path

from app_subscriptions.apps import AppSubscriptionsConfig
from app_subscriptions.views.course import SubscribeCourseAPIView

app_name = AppSubscriptionsConfig.name

urlpatterns = [
    path('course/<int:pk>', SubscribeCourseAPIView.as_view(), name="subscribe_course"),
]
