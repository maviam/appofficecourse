from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'page_title': 'Office Course'
    }
    return render(
        request,
        'course/index.html',
        context
    )