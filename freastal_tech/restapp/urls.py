from django.urls import path

from .views import StudentDetail

urlpatterns = [
    path('student/<int:pk>/', StudentDetail.as_view(), name="student")
]
