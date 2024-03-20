import os

from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from core.tasks import process_and_send_image


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ImageData(models.Model):
    image_data = models.BinaryField()
    image_path = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @receiver(post_save)
    def trigger_image_data_processing(sender, instance, created, **kwargs):
        if created:
            image_path = os.path.join(settings.MEDIA_ROOT, instance.image_path)
            process_and_send_image.delay(image_path)




