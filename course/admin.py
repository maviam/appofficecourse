from django.contrib import admin
from course import models

# Register your models here.
@admin.register(models.TrainingUnit)
class TrainingUnitAdmin(admin.ModelAdmin):
    list_display = ('code','subject','period','active',)
    ordering = ('-subject',)
    search_fields = ('code','subject',)
    