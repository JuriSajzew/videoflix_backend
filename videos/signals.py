from .models import Video
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
import os


@receiver(post_save, sender=Video)
def video_post_save(sender, instance, created, **kwargs):
    print('Video wurde gespeichert')
    if created:
        print('New video created')

@receiver(post_delete, sender=Video)       
def video_delete_save(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `Video` object is deleted.
    """
    if instance.video_file:
        if os.path.isfile(instance.video_file.path):
            os.remove(instance.video_file.path)