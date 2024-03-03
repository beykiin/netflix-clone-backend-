from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Kategoriler(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
class Tur(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Izlenenler(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    izlenen=models.ManyToManyField("Movies")
    def __str__(self):
        return self.user.username
    
class Movies(models.Model):
    isim=models.CharField(max_length=200)
    aciklama=models.TextField(max_length=500)
    tur=models.ManyToManyField("Tur",null=True)
    afis=models.FileField(upload_to='afis')
    kategori=models.ForeignKey(Kategoriler,on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self):
        return self.isim
    
# class YourModel(models.Model):
#     title = models.CharField(max_length=255)
#     release_date = models.DateField()
#     description = models.TextField()

#     def __str__(self):
#         return self.title