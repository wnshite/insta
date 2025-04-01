from django.db import models
from django.contrib.auth.models import AbstractUser
from django_resized import ResizedImageField

# Create your models here.
class User(AbstractUser):
    profile_image = ResizedImageField(
        size=[500, 500],
        crop=['middle', 'center'],
        upload_to='profile',
    )

    followings = models.ManyToManyField('self', related_name='followers', symmetrical=False)  # 내가 팔로우를 한 사람들.
    # followers = 

