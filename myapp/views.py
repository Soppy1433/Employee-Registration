from django.shortcuts import render, redirect
from .models import Employee

def index(request):
    if request.method == "POST":
        id = request.POST["employee_id"]
        email = request.POST["email_id"]
        name = request.POST["name"]
        mobile_number = request.POST["mobile_number"]
        address = request.POST["address"]
        employee = Employee(name=name, employee_id=empid, email_id=email, mobile_number=mobile_number, address=address)
        employee.save()

    employees = Employee.objects.all()
    context = {
        "employees": employees
    }
    return render(request, "index.html", context)


def delete_employee(request, empid):
    employee = Employee.objects.get(employee_id=empid)
    employee.delete()
    return redirect(index)

def update_employee(request, employee_id):
    employee = Employee.objects.get(employee_id=empid)
    context = {
        "employee": employee
    }
    return render(request, "update_employee.html", context)

def update(request, empid):
    if request.method == "POST":
        employee = Employee.objects.get(employee_id=empid)
        employee.name = request.POST.get("name")
        employee.employee_id = request.POST.get("employee_id")
        employee.mobile_number = request.POST.get("mobile_number")
        employee.address = request.POST.get("address")
        employee.email_id = request.POST.get("email_id")
        employee.save()
    return redirect(index)