from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    profilName=models.CharField(max_length=100)
    profilImage=models.FileField(upload_to="profilImage")
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.profilName