import logging
from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.profiles.models import Employee,Patient
from preclinic.settings.development import AUTH_USER_MODEL

logger = logging.getLogger(__name__)


@receiver(post_save, sender=AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_patient:
            Patient.objects.create(user=instance)
            logger.info(f"{instance}'s patient profile created")

        elif instance.is_artisan:
            Employee.objects.create(user=instance)
            logger.info(f"{instance}'s employee profile created")
      
      

@receiver(post_save, sender=AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    if instance.is_patient:
        instance.patient.save()
        logger.info(f"{instance}'s patient profile saved")

    elif instance.is_employee:
        instance.employee.save()
        logger.info(f"{instance}'s employee profile saved")



   
