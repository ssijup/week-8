from django.db import models

# Create your models here.
class Userdetails(models.Model):
    user_name = models.CharField(max_length=50)
    user_email = models.CharField(max_length=100)
    user_password = models.CharField(max_length=50)

class Products(models.Model):
    book_title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    price = models.IntegerField()
    picture = models.ImageField(upload_to='productimg')


    

