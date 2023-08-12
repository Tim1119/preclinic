from .models import Course
from django.forms import ModelForm
class CourseForm(ModelForm):
    
    class Meta:

        model = Course
        fields=['name']

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})