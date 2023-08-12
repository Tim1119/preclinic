from django.db import models
# from apps.utilities.models import TimeStampedUUIDModel
from autoslug import  AutoSlugField
import uuid
# Create your models here.


class Course(models.Model):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=260,unique=True,verbose_name="Course of Study")
    slug = AutoSlugField(populate_from='name', unique=True)

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    def __str__(self):
        return self.name