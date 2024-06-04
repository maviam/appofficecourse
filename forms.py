from course.models import Student
from django import forms
from project import settings

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('name','birthday','sex','city','my_class','dropout')
        # fields = '__all__'
        labels = { 'my_class': 'Class'}
        widgets = {
            'birthday': forms.DateInput(
                attrs = {
                    'type': 'date'
                }
            )
        }