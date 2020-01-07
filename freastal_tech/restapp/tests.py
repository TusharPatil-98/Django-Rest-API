from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import StudentData
from .serializers import DataSerializer


class BaseTestView(APITestCase):
    client = APIClient()

    @staticmethod
    def create_student(name='', age=0, std=''):
        if name != "" and age !=0 and std != "":
            StudentData.objects.create(name=name, age=age, std=std)

    def setUp(self):
        self.create_student("Ram", 10, "Fifth")
        self.create_student("Sham", 15, "Tenth")
        self.create_student("John", 12, "Seventh")

class GetAllStudentsTest(BaseTestView):

    def test_get_all_students(self):
        response = self.client.get(
            reverse('student-all')
        )
        expected = StudentData.objects.all()
        serialized = DataSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)