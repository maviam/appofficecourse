from django.shortcuts import render, get_object_or_404, redirect
from course.models import Student, Grade
from forms import StudentForm
from django.core.paginator import Paginator

# Create your views here.
def list_of_students(request):
    students = Student.objects.all()
    paginator = Paginator(students, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_title': 'List of students',
        'page_obj': page_obj,
        'header': True
    }
    return render(
        request,
        'course/student/list.html',
        context
    )

def student_information(request, student_id):
    student = Student.objects.get(pk=student_id)
    grades = Grade.objects.filter(student=student_id).order_by('grade')
    context = {
        'page_title': 'List of students',
        'student': student,
        'grades': grades,
        'header': True
    }
    return render(
        request,
        'course/student/student.html',
        context
    )

def create_student(request, student_id = None):
    if student_id:
        student = get_object_or_404(Student, pk=student_id)
        title = "Edit Student"
        if request.method == 'POST':
            form = StudentForm(data = request.POST, instance=student)
            context = { 
                'page_title': 'Edit student',
                'form': form,
                'header': True,
                'student': student,
                'title': title,
                'button': 'Update student data'
            }
            
            if form.is_valid():
                form.save()
                return redirect('course:students_list')

            return render(
                request,
                'course/student/create.html',
                context
            )
        
        # If method s GET ...
        context = {
            'page_title': 'Add new student',
            'form': StudentForm(instance=student),
            'header': True,
            'student': student,
            'title': title,
            'button': 'Update student data'
        }
        return render(
            request,
            'course/student/create.html',
            context
        )
    else:
        title = "Add new student"
        if request.method == 'POST':
            form = StudentForm(data=request.POST)
            context = {
                'page_title': 'Add new student',
                'form': form,
                'header': True,
                'title': title,
                'button': 'Add student'
            }
            
            if form.is_valid():
                form.save()
                return redirect('course:students_list')

            return render(
                request,
                'course/student/create.html',
                context
            )
        
        context = {
            'page_title': 'Add new student',
            'form': StudentForm(),
            'header': True,
            'title': title,
            'button': 'Add student'
        }
        return render(
            request,
            'course/student/create.html',
            context
        )

def delete_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    
    student.delete()
    return redirect('course:students_list')

