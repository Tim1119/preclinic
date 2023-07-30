import uuid
from autoslug import AutoSlugField
from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

User = get_user_model()


class BaseProfile(models.Model):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('User'))
    profile_picture = ProcessedImageField(upload_to='avatars', processors=[ResizeToFill(100, 50)],format='JPEG',options={'quality': 60})
    profile_picture = models.ImageField(upload_to='profile_pictures', default='default.png', validators=[ FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg'])])
    phone_number = models.CharField( max_length=14,verbose_name=_("Phone Number"), default="+234524204242")
    slug = AutoSlugField(populate_from='user', unique=True)
    address = models.TextField(verbose_name=_('Your Address'))
    has_updated_profile = models.BooleanField( default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

