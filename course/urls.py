from django.urls import path
from course import views

app_name = 'course'

urlpatterns = [
    path('student/<int:student_id>/', views.student_information, name='see_student'),
    path('student/<int:student_id>/edit', views.create_student, name='edit_student'),
    path('student/<int:student_id>/delete', views.confirm_deletion_student, name='confirm_deletion_student'),
    path('student/<int:student_id>/accepted_delete/', views.delete_student, name='delete_student'),
    path('course/<int:class_id>', views.main_data, name='main_data'),
    path('course/student/', views.create_student, name='new_student'),
    path('student/list/', views.list_of_students, name='students_list'),
    path('course/training-unit', views.create_unit, name='new_unit'),
    path('training-unit/list/', views.list_of_training_units, name='units_list'),
    path('training-unit/<int:unit_code>', views.unit_information, name='see_unit'),
    path('', views.index, name='class_index')
]