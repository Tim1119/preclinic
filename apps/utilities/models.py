from django.db import models
import uuid
from django.utils.translation import gettext_lazy as _
from autoslug import AutoSlugField
from apps.profiles.models import Employee
from apps.course.models import Course
from apps.institution.models import Institution

class TimeStampedUUIDModel(models.Model):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True






