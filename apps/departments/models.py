from django.db import models
from apps.utilities.models import TimeStampedUUIDModel
from autoslug import  AutoSlugField
from django.utils.translation import gettext_lazy as _

class HospitalDepartments(TimeStampedUUIDModel):
    name = models.CharField(max_length=300)
    slug = AutoSlugField(populate_from='name', unique=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = _("Hospital Department")
        verbose_name_plural = _("Hospital Departments")