#  clean fields make appointments less or greater than today appointment_date__gt=datetime.now().date()
from datetime import date
from .models import AdminAppointment,Appointment,DoctorAppointment
from django.forms import ModelForm
from django.core.exceptions import ValidationError

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
        if appointment_date < date.today():
            raise ValidationError("You can't create an appointment before today")
        return appointment_date

class AdminAppointmentForm(ModelForm):
    
    class Meta:

        model = AdminAppointment
        exclude=['ref']

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['appointment'].widget.attrs.update({'class': 'form-control'})
        self.fields['start_time'].widget.attrs.update({'class': 'form-control col-md-6'})
        self.fields['end_time'].widget.attrs.update({'class': 'form-control col-md-6'})
        self.fields['cost'].widget.attrs.update({'class': 'form-control col-md-6'})
        self.fields['status'].widget.attrs.update({'class': 'form-control col-md-6'})
        self.fields['employee'].widget.attrs.update({'class': 'form-control'})


    
    # prevent admin from setting time for a time before now
    # def clean_start_time(self):
    #     start_time = self.cleaned_data['start_time']
    #     if start_time < date.:
    #         raise ValidationError("You can't create an appointment before today")
    #     return start_time
    
    # def clean_end_time(self):
    #     end_time = self.cleaned_data['end_time']
    #     if end_time < date.today():
    #         raise ValidationError("You can't create an appointment before today")
    #     return end_time
        



class DoctorAppointmentForm(ModelForm):
    
    class Meta:

        model = DoctorAppointment
        exclude=['ref','appointment']

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['symptoms'].widget.attrs.update({'class': 'form-control'})
        self.fields['recommendation'].widget.attrs.update({'class': 'form-control'})
        self.fields['drugs'].widget.attrs.update({'class': 'form-control'})
       
        