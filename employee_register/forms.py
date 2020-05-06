from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('fullName','emp_code','mobile','position')
        labels = {
            'fullName': 'Full Name',
            'emp_code': 'Employee Id',
            'mobile': 'Mobile',
            'position': 'Position'
    }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select"
