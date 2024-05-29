from django.db import models

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