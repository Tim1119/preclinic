import logging
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Appointment,AdminAppointment,DoctorAppointment
from preclinic.settings.development import AUTH_USER_MODEL

logger = logging.getLogger(__name__)


@receiver(post_save, sender=Appointment)
def create_user_admin_appointment(sender, instance, created, **kwargs):
    if created:
        AdminAppointment.objects.create(appointment=instance)
        logger.info(f"{instance}'s admin appointment created")

        DoctorAppointment.objects.create(appointment=instance)
        logger.info(f"{instance}'s doctor's appointment created")
    
      

@receiver(post_save, sender=Appointment)
def save_user_admin_appointment(sender, instance, **kwargs):
    instance.adminappointment.save()
    logger.info(f"{instance}'s admin appointment saved")
    instance.doctorappointment.save()
    logger.info(f"{instance}'s doctor appointment saved")
    



   
