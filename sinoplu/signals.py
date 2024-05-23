from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from .models import Sinopluyuz
from .utils import get_random_code

@receiver(pre_save, sender=Sinopluyuz)
def pre_save_create_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.first_name + " " + get_random_code())
        