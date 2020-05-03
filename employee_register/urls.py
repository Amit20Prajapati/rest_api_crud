from django.conf.urls import url,include
from . import views

urlpatterns = [
    url('form/', views.employee_form), #localhost:p/employee/list
    url('form/<int:id>/', views.employee_form, name="employee_update"),
    url('list/', views.employee_list, name="employee_list"),

]
