from django.urls import path

from .views import ListStudentsView, StudentDetail

urlpatterns = [
    path('student/<int:pk>/', StudentDetail.as_view(), name="student")
]
