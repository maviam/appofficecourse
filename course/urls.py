from django.urls import path
from course import views

app_name = 'course'

urlpatterns = [
    path('student/<int:student_id>/', views.student_information, name='see_student'),
    path('course/<int:class_id>', views.main_data, name='main_data'),
    path('course/student/', views.create_student, name='new_student'),
    path('student/list/', views.list_of_students, name='students_list'),
    path('training-unit/list/', views.list_of_training_units, name='units_list'),
    path('', views.index, name='class_index')
]