from .models import AdminAppointment,Appointment,DoctorAppointment
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.utils import timezone
from apps.profiles.models import Employee
class PatientAppointmentForm(ModelForm):
    
    class Meta:

        model = Appointment
        exclude=['ref','created_by','completed']

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['appointment_date'].widget.attrs.update({'class': 'form-control'})
        self.fields['department'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})

    def clean_appointment_date(self):
        appointment_date = self.cleaned_data['appointment_date']
        if appointment_date  and appointment_date < timezone.now().date()+ timezone.timedelta(days=1):
            raise ValidationError("You can't create an appointment before today. You can only book an appointment from tomorrow onwards")
        return appointment_date

class AdminAppointmentForm(ModelForm):
    
    class Meta:

        model = AdminAppointment
        exclude=['ref','appointment']

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['start_time'].widget.attrs.update({'class': 'form-control'})
        self.fields['end_time'].widget.attrs.update({'class': 'form-control'})
        self.fields['cost'].widget.attrs.update({'class': 'form-control'})
        self.fields['status'].widget.attrs.update({'class': 'form-control'})
        self.fields['employee'].widget.attrs.update({'class': 'form-control'})

     
        self.fields['employee'].queryset = Employee.objects.filter(role='Doctor')

    def clean_employee(self):
        employee = self.cleaned_data.get('employee')
        if employee and not employee.role == 'Doctor':
            raise ValidationError("Only doctors can be assigned to appointments.")
        return employee


class DoctorAppointmentForm(ModelForm):
    
    class Meta:

        model = DoctorAppointment
        exclude=['ref','appointment']

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['symptoms'].widget.attrs.update({'class': 'form-control'})
        self.fields['recommendation'].widget.attrs.update({'class': 'form-control'})
        self.fields['drugs'].widget.attrs.update({'class': 'form-control'})
       
        