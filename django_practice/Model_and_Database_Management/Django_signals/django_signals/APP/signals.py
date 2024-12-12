from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import Product
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.utils.text import slugify

@receiver(pre_save, sender=Product)
def create_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)

@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        send_mail(
            'Welcome to the Site!',
            f'Hi {instance.username}, thank you for joining us.',
            'admin@example.com',
            [instance.email],
            fail_silently=False,
        )
