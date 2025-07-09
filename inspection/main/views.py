from django.shortcuts import render, get_object_or_404
from .models import JobTitle, Department, Gender, Employee

def employees_list(request):
    jobtitles = JobTitle.object.all()
    departments = Department.object.all()
    genders = Gender.object.all()
    employees = Employee.object.all()

    return render(request, 'main')