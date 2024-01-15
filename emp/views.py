from django.shortcuts import render,HttpResponse
from emp.models import employee,department,role
from django.db.models import Q

def index(request):
    return render(request,"index.html")


def add_emp(request):
    if request.method=="POST":
       firstname=request.POST['fname']  #fname is field name 
       lastname=request.POST['lname']
       dep=request.POST['department']
       salary=int(request.POST['salary'])
       role=request.POST['role']
       phone=request.POST['phone']    

       new_emp=employee(firstName=firstname,lastName=lastname,dept_id=dep, salary=salary,role_id=role,phone=phone)
       #one firstname is model field name and another is varibale which we declare above

       new_emp.save()
       return HttpResponse("Employee Add Succeefully")


    return render(request,"add_emp.html")


def filter_emp(request):

    if request.method=="POST":
        name=request.POST['fullname']
        dept=request.POST['dep']
        role=request.POST['role']
        emps=employee.objects.all()
        if name:
            emps=emps.filter(Q(firstName__icontains=name) | Q(lastName__icontains=name))

        if dept:
            emps=emps.filter(dept__name__icontains=dept)
        
        if role:
            emps=emps.filter(role__name__icontains=role)
        context={
            "emp":emps
        }
        return render(request,"all_emp.html",context)
    return render(request,"filter.html")

def remove_emp(request,emp_id=0):
    if emp_id:
        emp =employee.objects.get(id=emp_id)
        emp.delete()
        return HttpResponse(f"Employee {emp.firstName} has been removed")
    employees=employee.objects.all()
    context={
        "emps":employees
    }
    
    return render(request,"removeemp.html",context)





def all_emp(request):
    emps=employee.objects.all()      #this employee is models

    context={
        'emp':emps         #emp is is key which we can use through for loop
    }
   # print(context)
    return render(request,"all_emp.html", context)






def index(request):
    return render(request,"index.html")

# Create your views here.
