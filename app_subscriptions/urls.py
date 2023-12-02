from django.urls import path

from app_pwl.apps import AppPwlConfig


app_name = AppPwlConfig.name

urlpatterns = [
    path('course/<int:pk>', SubscribeCourseAPIView.as_view(), name="subscribe_course"),
]
