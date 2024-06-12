from django.db import models
from django.utils import timezone


# Create your models here.
class TrainingUnit(models.Model):
    code = models.CharField(max_length=5, primary_key=True)
    subject = models.CharField(max_length=50)
    hours = models.SmallIntegerField(choices=[(25,"25 hours"),(30,"30 hours"),(50,"50 hours"),(75,"75 hours")])
    period = models.SmallIntegerField(choices=[(1,"First period"),(2,"Second period"),(3,"Third period")])
    all_classes = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.code}- { self.subject}'

class Class(models.Model):
    class Meta:
        verbose_name = 'Class'
        verbose_name_plural = 'Classes'
    
    acronym = models.CharField(max_length=2)
    name = models.CharField(max_length=75, blank=True)
    picture = models.ImageField(blank=True,upload_to='pictures/%Y/%m/')
    closed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.acronym}'

class ClassesUnit(models.Model):
    unit = models.ForeignKey(TrainingUnit, on_delete=models.CASCADE)
    unit_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    
    class Meta: 
        verbose_name = 'Classes Unit'
        verbose_name_plural = 'Classes Units'
        constraints = [
            models.UniqueConstraint(
                fields=['unit', 'unit_class'], name='unique_unit_class_combination'
            )
        ]
    
    def __str__(self):
        return f'{self.unit_class}- {self.unit}'

class Student(models.Model):    
    name = models.CharField(max_length=100)
    birthday = models.DateField()
    sex = models.CharField(
                    max_length=6, 
                    choices=[
                                ('F','Female'),
                                ('M','Male')
                            ]
                    )
    city = models.CharField(
                    max_length=20, 
                    blank=True,
                    choices=[
                                ('FML','Famalicão'),
                                ('FRM','Freamunde'),
                                ('PFR','Paços de Ferreira'),
                                ('STR','Santo Tirso')
                            ]
                    )
    dropout = models.BooleanField(default=False)
    my_class = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return f'{self.name}'
    
class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    training_unit = models.ForeignKey(TrainingUnit, on_delete=models.SET_NULL, null=True)
    grade = models.FloatField()
    released_date = models.DateTimeField(default=timezone.now)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['student', 'training_unit'], name='unique_student_unit_combination'
            )
        ]
    
    def __str__(self):
        return f'{self.student} - {self.training_unit} ({self.grade})'
