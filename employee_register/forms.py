from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        labels = {
            'fullname': 'Full Name',
            'emp_code': 'Employee Id',
            'mobile': 'Mobile',
            'position': 'Position'
    }

def __init__(self, *args, **kwargs):
    super(EmployeeForm, self).__init__(*args, **kwargs)
    self.fields['position'].label = "Select"
