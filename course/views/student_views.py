from django.shortcuts import render
from course.models import Student
from django import forms

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('name','birthday','sex','city','dropout','_class')

# Create your views here.
def create_student(request):
    
    context = {
        'page_title': 'Add new student',
        'form': StudentForm(),
        'header': True
    }
    return render(
        request,
        'course/student/create.html',
        context
    )