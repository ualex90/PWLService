from django.urls import path

from app_pwl.apps import AppPwlConfig
from app_subscriptions.views.course import SubscribeCourseAPIView

app_name = AppPwlConfig.name

urlpatterns = [
    path('course/<int:pk>', SubscribeCourseAPIView.as_view(), name="subscribe_course"),
]
