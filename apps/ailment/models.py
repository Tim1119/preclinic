from django.db import models
from apps.utilities.models import TimeStampedUUIDModel
from autoslug import AutoSlugField


class Ailment(TimeStampedUUIDModel):
    name = models.CharField(max_length=300,unique=True)
    slug = AutoSlugField(populate_from='name', unique=True)
    
    def __str__(self):
        return self.name
