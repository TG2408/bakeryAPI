# Generated by Django 3.1.7 on 2021-11-03 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apimain', '0003_auto_20211103_1722'),
    ]

    operations = [
        migrations.CreateModel(
            name='IngridientQuantity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ingridients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingridient', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=100)),
                ('cost_price', models.IntegerField()),
                ('selling_price', models.IntegerField()),
                ('all_ingridient', models.ManyToManyField(through='apimain.IngridientQuantity', to='apimain.Ingridients')),
            ],
        ),
        migrations.RemoveField(
            model_name='membership',
            name='group',
        ),
        migrations.RemoveField(
            model_name='membership',
            name='person',
        ),
        migrations.DeleteModel(
            name='Group',
        ),
        migrations.DeleteModel(
            name='Membership',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.AddField(
            model_name='ingridientquantity',
            name='ingridient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apimain.ingridients'),
        ),
        migrations.AddField(
            model_name='ingridientquantity',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apimain.products'),
        ),
    ]
