from videos.tasks import convert_all_resolutions
from .models import Video
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
import os


@receiver(post_save, sender=Video)
def video_post_save(sender, instance, created, **kwargs):
    print('Video wurde gespeichert')
    if created:
        print('New video created')
        convert_all_resolutions(instance.video_file.path)
        #convert_720p(instance.video_file.path)

@receiver(post_delete, sender=Video)       
def video_delete_save(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `Video` object is deleted.
    """
    if instance.video_file:
        if os.path.isfile(instance.video_file.path):
            os.remove(instance.video_file.path)