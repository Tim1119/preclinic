from django.db import models
import uuid
from django.utils.translation import gettext_lazy as _
from autoslug import AutoSlugField

class TimeStampedUUIDModel(models.Model):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# Create your models here.
class Institution(TimeStampedUUIDModel):
    name = models.CharField(max_length=260,unique=True,verbose_name=_("Name of Institution"))
    slug = AutoSlugField(populate_from='name', unique=True)

    class Meta:
        verbose_name = "Institution"
        verbose_name_plural = "Institutions"

    def __str__(self):
        return self.name

class Course(TimeStampedUUIDModel):
    name = models.CharField(max_length=260,unique=True,verbose_name=_("Course of Study"))
    slug = AutoSlugField(populate_from='name', unique=True)

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    def __str__(self):
        return self.name


class EducationInformation(TimeStampedUUIDModel):
    institution = models.ForeignKey(Institution,on_delete=models.SET_NULL,null=True,verbose_name=_("Name of Institution"))
    course_of_study = models.ForeignKey(Course,on_delete=models.SET_NULL,null=True,verbose_name=_("Course of Study"))
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        verbose_name = _("Education Information")
        verbose_name_plural = _("Education Information")


class WorkExperience(TimeStampedUUIDModel):
    title = models.CharField(max_length=260)
    description_of_work_experience = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True,null=True,help_text="Leave blank if you're still working there")

    class Meta:
        verbose_name = _("Education Information")
        verbose_name_plural = _("Education Information")


