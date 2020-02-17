from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny,IsAuthenticated
from student.models import Student
from student.serializer import stud_ser

class stu_op(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset =Student.objects.all()
    serializer_class = stud_ser
