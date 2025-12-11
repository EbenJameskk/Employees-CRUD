# from django.urls import path
# from . import views
# # from .views import EmployeeList, EmployeeCreate, EmployeeDelete, EmployeeUpdate, EmployeeView
#
# urlpatterns = [
#     path('addtask/', views.EmployeeCreate.as_view()),
#     path('getalldata/', EmployeeView),
#     path('updatedata/', EmployeeUpdate),
#     path('deldata/', EmployeeDelete),
#     path('list/', EmployeeList),
# ]

from django.urls import path

from employee_details import views

urlpatterns = [
    path('', views.employee_list, name='employee_list'),
    path('view/<int:pk>/', views.employee_view, name='employee_view'),
    path('new/', views.employee_create, name='employee_new'),
    path('edit/<int:pk>/', views.employee_update, name='employee_edit'),
    path('delete/<int:pk>/', views.employee_delete, name='employee_delete')

]

