from django.conf.urls import url,include
from . import views

urlpatterns = [
    url('list/', views.employee_list, name="employee_list"),
    # url('<int:id>/', views.employee_form, name='employee_update'),
    url('form/', views.employee_form, name="employee_insert"),  # localhost:p/employee/form
    # url('delete/<int:id>/', views.employee_delete, name="employee_delete")
]
