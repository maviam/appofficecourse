from django.shortcuts import render, redirect
from course.models import TrainingUnit
from django import forms
from django.core.paginator import Paginator
from forms import TrainingUnitForm

def list_of_training_units(request):
    units = TrainingUnit.objects.all()
    paginator = Paginator(units, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_title': 'List of training units',
        'page_obj': page_obj,
        'header': True
    }
    return render(
        request,
        'course/training_unit/list.html',
        context
    )

def unit_information(request, unit_code):
    unit = TrainingUnit.objects.get(pk=unit_code)
    context = {
        'page_title': 'Training unit information',
        'unit': unit,
        'header': True
    }
    return render(
        request,
        'course/training_unit/unit.html',
        context
    )

def create_unit(request):
    title = "Add new training unit"
    if request.method == 'POST':
        form = TrainingUnitForm(data=request.POST)
        context = {
            'page_title': 'Add new unit',
            'form': form,
            'header': True,
            'title': title,
        }
        
        if form.is_valid():
            form.save()
            return redirect('course:units_list')

        return render(
            request,
            'course/training_unit/create.html',
            context
        )
    
    context = {
        'page_title': 'Add new unit',
        'form': TrainingUnitForm(),
        'header': True,
        'title': title,
    }
    return render(
        request,
        'course/training_unit/create.html',
        context
    )