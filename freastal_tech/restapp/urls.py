from django.urls import path

from .views import ListStudentsView, StudentDetail

urlpatterns = [
    path('students/', ListStudentsView.as_view(), name="student-all"),
    path('student/<int:pk>/', StudentDetail.as_view(), name="student")
]