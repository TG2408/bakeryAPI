from rest_framework import fields, serializers
from rest_framework.compat import md_filter_add_syntax_highlight
from . models import Admin, Customer, Inventory, IngredientQuantity, Products

class AdminSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ['username', 'password']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['username', 'password']

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ['ingredient']

class IngredientQuantitySerialzer(serializers.ModelSerializer):
    class Meta:
        model = IngredientQuantity
        fields = ['inventory', 'product', 'quantity']

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['product', 'cost_price', 'selling_price', 'all_ingridient']

 


    # def create(self, validated_data):
    #     """
    #     Create and return a new `Snippet` instance, given the validated data.
    #     """
    #     return Inventory.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `Snippet` instance, given the validated data.
    #     """
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.code = validated_data.get('code', instance.code)
    #     instance.linenos = validated_data.get('linenos', instance.linenos)
    #     instance.language = validated_data.get('language', instance.language)
    #     instance.style = validated_data.get('style', instance.style)
    #     instance.save()
    #     return instance

