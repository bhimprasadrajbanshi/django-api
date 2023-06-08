from django.shortcuts import render
from .models import student
from .serializers import studentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

# Create your views here.
def studen_details(request, pk):
    std = student.objects.get(id=pk)
    serializer = studentSerializer(std)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')