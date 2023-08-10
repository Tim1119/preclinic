#  clean fields make appointments less or greater than today appointment_date__gt=datetime.now().date()
from datetime import date
from .models import Employee,Patient
from django.forms import ModelForm
from django.core.exceptions import ValidationError

class PatientProfileForm(ModelForm):
    
    class Meta:

        model = Patient
        exclude = ['user','has_updated_profile']

         
    def clean_recipients(self):
        appointment_date = self.cleaned_data['appointment_date']
        if appointment_date < date.today():
            raise ValidationError("You can't create an appointment before today")
        return appointment_date
    
    def __init__(self, *args, **kwargs):
        super(PatientProfileForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.widget.attrs.get('class'):
                field.widget.attrs['class'] += ' form-control'
            else:
                field.widget.attrs['class'] = 'form-control'

class EmployeeProfileForm(ModelForm):
    
    class Meta:

        model = Employee
        exclude = ['user','has_updated_profile','is_approved']
    
    def __init__(self, *args, **kwargs):
        super(EmployeeProfileForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.widget.attrs.get('class'):
                field.widget.attrs['class'] += ' form-control'
            else:
                field.widget.attrs['class'] = 'form-control'
