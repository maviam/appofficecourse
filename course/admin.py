from django.contrib import admin
from course import models

# Register your models here.
@admin.register(models.TrainingUnit)
class TrainingUnitAdmin(admin.ModelAdmin):
    list_display = ('code','subject','period','all_classes',)
    ordering = ('-subject',)
    search_fields = ('code','subject',)

@admin.register(models.Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('acronym',)
    ordering = ('acronym',)

@admin.register(models.ClassesUnit)
class UnitsClassAdmin(admin.ModelAdmin):
    list_display = ('unit','unit_class',)
    ordering = ('unit_class',)

@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','name','birthday','my_class',)
    ordering = ('name',)
    search_fields = ('name',)

@admin.register(models.Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('student','training_unit','grade',)
    ordering = ('-training_unit',)
    search_fields = ('training_unit',)