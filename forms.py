from course.models import Student, TrainingUnit
from django import forms
from project import settings
from django.core.exceptions import ValidationError

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

    # def clean(self):
    #     self.add_error(
    #         'name',
    #         ValidationError(
    #             'Existe algum erro neste campo',
    #             code = 'invalid'
    #         )
    #     )
    #     return super().clean()
    
class TrainingUnitForm(forms.ModelForm):
    class Meta:
        model = TrainingUnit
        fields = ('code','subject','hours','period','all_classes')
