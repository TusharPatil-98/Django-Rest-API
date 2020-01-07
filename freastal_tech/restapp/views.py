from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from .serializers import DataSerializer
from .models import StudentData


# Create your views here.
class ListStudentsView(APIView):
    #queryset = StudentData.objects.all()
    #serializer_class = DataSerializer
    def get(self, request, format=None):
        queryset = StudentData.objects.all()
        serializer_class = DataSerializer(queryset, many=True)
        return Response(serializer_class.data)

    def post(self, request, format=None):
        serializer = DataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentDetail(APIView):
    def get_object(self, pk):
        try:
            return StudentData.objects.get(pk=pk)
        except StudentData.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk=pk)
        user = DataSerializer(user)
        return Response(user.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk=pk)
        serializer = DataSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
