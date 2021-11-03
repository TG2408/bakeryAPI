from django.db import models

# Create your models here.
class Ingridients(models.Model):
    ingridient = models.CharField(max_length=50)

    def __str__(self):
        return self.ingridient

class Products(models.Model):
    product = models.CharField(max_length=100)
    cost_price = models.IntegerField()
    selling_price = models.IntegerField()
    all_ingridient = models.ManyToManyField(
        Ingridients,
        through='IngridientQuantity'
        #verbose_name="all ingriedients",
    )

    def __str__(self):
        return self.product

class IngridientQuantity(models.Model):
    ingridient = models.ForeignKey(Ingridients, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.ingridient} in {self.product} (g)"

# class Person(models.Model):
#     name = models.CharField(max_length=128)

#     def __str__(self):
#         return self.name

# class Group(models.Model):
#     name = models.CharField(max_length=128)
#     members = models.ManyToManyField(Person, through='Membership')

#     def __str__(self):
#         return self.name

# class Membership(models.Model):
#     person = models.ForeignKey(Person, on_delete=models.CASCADE)
#     group = models.ForeignKey(Group, on_delete=models.CASCADE)
#     date_joined = models.DateField()
#     invite_reason = models.CharField(max_length=64)