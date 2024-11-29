from django.shortcuts import render
from graduates.models import GraduatingStudents, Category



def graduates(request):
    context = {
        "graduates": GraduatingStudents.objects.all(),
        "category": Category.objects.all()
    }
    return render(request, "graduates/graduatingstudents.html", context)

def graduates_by_category(request, slug):
    context = {
        "graduates": GraduatingStudents.objects.filter(category__slug=slug),
        "category": Category.objects.all()
    }
    return render(request, "graduates/graduatingstudents.html", context)