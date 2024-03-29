from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	portfolio_site = models.URLField()
	profile_pic = models.ImageField(upload_to="profile_pics", default="default.png")