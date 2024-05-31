from django.shortcuts import render
from course.models import Class

# Create your views here.
def index(request):
    classes = Class.objects.all()
    context = {
        'page_title': 'Office Course',
        'classes': classes
    }
    return render(
        request,
        'course/index.html',
        context
    )