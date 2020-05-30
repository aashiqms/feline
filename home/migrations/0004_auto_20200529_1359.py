# Generated by Django 3.0.6 on 2020-05-29 20:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_image_imageuploader_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='imageuploader_profile',
            new_name='author',
        ),
        migrations.AddField(
            model_name='image',
            name='posted_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]