from django.db import models

# Create your models here.
food_choice = [
        ('Veg', 'Veg'),
        ('Non-Veg', 'Non-Veg'),

    ]
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
    image1 = models.ImageField(upload_to='tiffin/images')
    image2 = models.ImageField(upload_to='tiffin/images')
    image3 = models.ImageField(upload_to='tiffin/images',  verbose_name='image')

    def __str__(self):
        return self.name
    
class Breakfast(models.Model):
    id = models.AutoField(primary_key=True)
    sun = models.CharField(max_length=100)
    mon = models.CharField(max_length=100)
    tue = models.CharField(max_length=100)
    wed = models.CharField(max_length=100)
    thu = models.CharField(max_length=100)
    fri = models.CharField(max_length=100)
    sat = models.CharField(max_length=100)
    price = models.IntegerField()
    food_type = models.CharField(max_length=10, choices=food_choice, default="Veg")

class Lunch(models.Model):
    id = models.AutoField(primary_key=True)
    sun = models.CharField(max_length=100)
    mon = models.CharField(max_length=100)
    tue = models.CharField(max_length=100)
    wed = models.CharField(max_length=100)
    thu = models.CharField(max_length=100)
    fri = models.CharField(max_length=100)
    sat = models.CharField(max_length=100)
    price = models.IntegerField()
    food_type = models.CharField(max_length=10, choices=food_choice, default="Veg")

class Dinner(models.Model):
    id = models.AutoField(primary_key=True)
    sun = models.CharField(max_length=100)
    mon = models.CharField(max_length=100)
    tue = models.CharField(max_length=100)
    wed = models.CharField(max_length=100)
    thu = models.CharField(max_length=100)
    fri = models.CharField(max_length=100)
    sat = models.CharField(max_length=100)
    price = models.IntegerField()
    food_type = models.CharField(max_length=10, choices=food_choice, default="Veg")

class Menu_card(models.Model):
    id = models.AutoField(primary_key=True)
    kitchen = models.ForeignKey(kitchen, on_delete=models.CASCADE, default=None)
    breakfast =  models.ForeignKey(Breakfast, on_delete=models.CASCADE, default=None)
    lunch =  models.ForeignKey(Lunch, on_delete=models.CASCADE, default=None)
    dinner =  models.ForeignKey(Dinner, on_delete=models.CASCADE, default=None)


    