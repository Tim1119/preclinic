from .models import AdminAppointment,Appointment,DoctorAppointment
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.utils import timezone
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

    def clean_recipients(self):
        appointment_date = self.cleaned_data['appointment_date']
        if appointment_date  and appointment_date < timezone.now().date()+ timezone.timedelta(days=1):
            raise ValidationError("You can't create an appointment before today")
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


class DoctorAppointmentForm(ModelForm):
    
    class Meta:

        model = DoctorAppointment
        exclude=['ref','appointment']

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['symptoms'].widget.attrs.update({'class': 'form-control'})
        self.fields['recommendation'].widget.attrs.update({'class': 'form-control'})
        self.fields['drugs'].widget.attrs.update({'class': 'form-control'})
       
        