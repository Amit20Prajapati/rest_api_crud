from django.conf.urls import url,include
from . import views

urlpatterns = [
    url('list/', views.employee_list),
    url('<int:id>/', views.employee_form, name='employee_update'),
    url('/', views.employee_form, name="employee_from"),  # localhost:p/employee/form
]
