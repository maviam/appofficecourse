from django.db import models
from django.utils import timezone


# Create your models here.
class TrainingUnit(models.Model):
    code = models.CharField(max_length=5, primary_key=True)
    subject = models.CharField(max_length=50)
    hours = models.SmallIntegerField()
    period = models.SmallIntegerField()
    active = models.BooleanField(default=True)
    picture = models.ImageField(blank=True,upload_to='pictures/%Y/%m/')
    
    def __str__(self):
        return f'{self.code} - { self.subject}'

class Class(models.Model):
    acronym = models.CharField(max_length=2)


class Student(models.Model):
    name = models.CharField(max_length=100)
    birthday = models.DateField()
    sex = models.CharField(max_length=6, choices=[('F','Female'),('M','Male')])
    _class = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True)
    
class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    training_unit = models.ForeignKey(TrainingUnit, on_delete=models.SET_NULL, null=True)
    grade = models.FloatField()
    released_date = models.DateTimeField(default=timezone.now)