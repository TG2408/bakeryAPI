from django.db import models

# Create your models here.

class Inventory(models.Model):
    ingredient = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.ingredient}(pk={self.pk})"

class Products(models.Model):
    product = models.CharField(max_length=100)
    cost_price = models.IntegerField()
    selling_price = models.IntegerField()
    all_ingridient = models.ManyToManyField(
        Inventory,
        through='IngredientQuantity'
        #verbose_name="all ingriedients",
    )

    def __str__(self):
        return f"{self.product}(pk={self.pk})"

class IngredientQuantity(models.Model):
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.product} {self.inventory} {self.quantity}g(pk={self.pk})"

