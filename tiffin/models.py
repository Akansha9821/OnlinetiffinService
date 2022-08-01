from django.db import models

# Create your models here.
class tiffin_user(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    add1 = models.CharField(max_length=100)
    add2 = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.IntegerField()

    def __str__(self):
        return self.name


class kitchen(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    pincode = models.IntegerField()
    image1 = models.ImageField(upload_to='tiffin/images',  verbose_name='image')
    
