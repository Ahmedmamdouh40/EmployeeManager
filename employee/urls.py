"""employee_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from employee import views


urlpatterns = [
     path('add_employee', views.create_employee),
     path('' , views.employees_list),
     path('edit_employee/<employee_id>' , views.edit_employee),
     path('delete_employee/<employee_id>',views.delete_employee),


     path('positions',views.positions_list),
     path('positions/add_position',views.create_position),
     path('positions/edit_position/<position_id>',views.edit_position),
     path('positions/delete_position/<position_id>',views.delete_position),


     path('departments',views.departments_list),
     path('departments/add_department',views.create_department),
     path('departments/edit_department/<department_id>' , views.edit_department),
     path('departments/delete_department/<department_id>' , views.delete_department)
]
