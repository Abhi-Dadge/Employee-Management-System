from django.shortcuts import render, HttpResponse
from emp_app.models import Employee, Department, Role
from datetime import datetime
from django.db.models import Q

# Home page
def index(request):
    return render(request, 'emp_app/home.html')

# Show all employees
def all_emp(request):
    emps = Employee.objects.all()
    context = {'emps': emps}
    return render(request, 'emp_app/all_emp.html', context)

# Add an employee
def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        location = request.POST['location'].strip()  # ✅ Corrected and added

        dept_name = request.POST['dept'].strip()
        role_name = request.POST['role'].strip()

        # Get or create department
        dept, _ = Department.objects.get_or_create(name=dept_name)

        # Get or create role
        role, _ = Role.objects.get_or_create(name=role_name)

        # Create employee
        new_emp = Employee(
            first_name=first_name,
            last_name=last_name,
            salary=salary,
            bonus=bonus,
            phone=phone,
            location=location,  # ✅ Added here
            dept=dept,
            role=role,
            hire_date=datetime.now()
        )
        new_emp.save()
        return HttpResponse('✅ Employee added successfully!')

    elif request.method == 'GET':
        return render(request, 'emp_app/add_emp.html')

    else:
        return HttpResponse('❌ An Exception Occurred. Employee Not Added.')

# Remove employee
def remove_emp(request, emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse('✅ Employee Record Deleted Successfully')
        except:
            return HttpResponse('❌ Please Enter A Valid Employee ID')

    emps = Employee.objects.all()
    context = {'emps': emps}
    return render(request, 'emp_app/remove_emp.html', context)

# Filter employees
def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']

        emps = Employee.objects.all()

        if name:
            emps = emps.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        if dept:
            emps = emps.filter(dept__name__icontains=dept)
        if role:
            emps = emps.filter(role__name__icontains=role)

        context = {'emps': emps}
        return render(request, 'emp_app/all_emp.html', context)

    elif request.method == 'GET':
        return render(request, 'emp_app/filter_emp.html')

    else:
        return HttpResponse('❌ An Exception Occurred')
