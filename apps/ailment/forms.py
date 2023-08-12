from django.forms import ModelForm
from .models import Ailment

class AilmentForm(ModelForm):
    
    class Meta:
        model = Ailment
        fields=['name']

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
      




        