from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	position = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	profile_pic = models.ImageField(default="profile1.png", upload_to='profile_pics', null=True, blank=True)

	def __str__(self):
		return f'{self.user}'