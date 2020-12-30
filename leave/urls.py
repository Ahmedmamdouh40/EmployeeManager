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
from leave import views


urlpatterns = [
     path('' , views.leave_masters_list),
     path('add_leave_master', views.create_leave_master),
     path('edit_leave_master/<leave_master_id>' , views.edit_leave_master),
     path('delete_leave_master/<leave_master_id>',views.delete_leave_master),

     path('employee_leaves' , views.employee_leaves_list),
     path('employee_leaves/add_employee_leave', views.create_employee_leave),
     path('employee_leaves/edit_employee_leave/<employee_leave_id>' , views.edit_employee_leave),
     path('employee_leaves/delete_employee_leave/<employee_leave_id>',views.delete_employee_leave),



]
