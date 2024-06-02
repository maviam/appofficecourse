from django.shortcuts import render
from course.models import Student
from django import forms

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('name','birthday','sex','city','my_class','dropout')

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

def list_of_students(request):
    students = Student.objects.all()
    context = {
        'page_title': 'List of students',
        'students': students,
        'header': True
    }
    return render(
        request,
        'course/student/list.html',
        context
    )

def student_information(request, student_id):
    student = Student.objects.get(pk=student_id)
    context = {
        'page_title': 'List of students',
        'student': student,
        'header': True
    }
    return render(
        request,
        'course/student/student.html',
        context
    )