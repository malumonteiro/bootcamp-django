from django.shortcuts import render
from django.http import HttpResponse
from .models import Course

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the bootcamp index.")

def course(request, course_id):
    get_course = Course.objects.filter(id=course_id)
    return HttpResponse("Ok %s." % get_course[0].name)
