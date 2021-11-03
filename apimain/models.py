from django.db import models

# Create your models here.
class ingridients(models.Model):
    ingridient = models.CharField(max_length=50)

class Products(models.Model):
    pass
