from rest_framework import fields, serializers
from rest_framework.compat import md_filter_add_syntax_highlight
from . models import Admin, customer, Inventory, IngredientQuantity, Products

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ['ingredient']

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
