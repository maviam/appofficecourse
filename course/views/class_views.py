from django.shortcuts import render
from course.models import Class, TrainingUnit, Student

# Create your views here.
def index(request):
    classes = Class.objects.all()
    context = {
        'page_title': 'Office Course',
        'classes': classes,
        'header': False
    }
    return render(
        request,
        'course/index.html',
        context
    )

def main_data(request,class_id):
    my_class = Class.objects.get(pk=class_id)
    students = Student.objects.filter(my_class=class_id)
    training_units = TrainingUnit.objects.all()
    context = {
        'page_title': 'Class Students and Training Units',
        'myclass': my_class,
        'students': students,
        'units': training_units,
        'header': True
    }
    return render(
        request,
        'course/main_data.html',
        context
    )