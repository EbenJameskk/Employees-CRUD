# from django.shortcuts import render
# from django.views.decorators.csrf import csrf_exempt
# # Create your views here.
# from django.http import HttpResponse
# from django.views.generic import ListView, DetailView
# from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.urls import reverse_lazy
# from .models import Employee

from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django.views.decorators.csrf import csrf_exempt

from .models import Employee


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'employee_id', 'email']


def employee_list(request, template_name='employee_details/employee_list.html'):
    employee = Employee.objects.all()
    data = {}
    data['object_list'] = employee
    return render(request, template_name, data)


def employee_view(request, pk, template_name='employee_details/employee_detail.html'):
    employee= get_object_or_404(Employee, pk=pk)
    return render(request, template_name, {'object':employee}) 
def employee_create(request, template_name='employee_details/employee_form.html'):
    form = EmployeeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('employee_list')
    return render(request, template_name, {'form':form})


def employee_update(request, pk, template_name='employee_details/employee_form.html'):
    employee= get_object_or_404(Employee, pk=pk)
    form = EmployeeForm(request.POST or None, instance=employee)
    if form.is_valid():
        form.save()
        return redirect('employee_list')
    return render(request, template_name, {'form':form})


def employee_delete(request, pk, template_name='employee_details/employee_confirm_delete.html'):
    employee= get_object_or_404(Employee, pk=pk)
    if request.method=='POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, template_name, {'object':employee})