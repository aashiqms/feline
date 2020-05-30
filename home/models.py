from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.http import request
from django.urls import reverse
from django.utils import timezone

from users.models import Profile


class Image(models.Model):
    image = models.ImageField(upload_to='media/user_uploads')
    image_description = models.CharField(max_length=100)
    tag_someone = models.CharField(max_length=50, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                                              null='True', blank=True)
    posted_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.image_description

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})



