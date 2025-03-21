from django.shortcuts import render
from .models import Department, Employee

def department_tree(request):
    departments = Department.objects.all()
    root_dept = Department.objects.get(parent__isnull=True)
    return render(request, 'employees/department_tree.html', {
        'root_dept': root_dept,
    })