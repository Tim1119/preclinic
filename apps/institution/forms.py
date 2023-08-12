from django.forms import ModelForm
from .models import Institution

class InstitutionForm(ModelForm):
    
    class Meta:
        model = Institution
        fields=['name']

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})




        