# Generated by Django 5.0.7 on 2024-09-02 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0003_video_video_urls'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='covers'),
        ),
    ]