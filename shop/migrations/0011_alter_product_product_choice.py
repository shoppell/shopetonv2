# Generated by Django 4.0.2 on 2022-03-18 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_remove_myshop_time_created_remove_wishlist_time_add_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_choice',
            field=models.ManyToManyField(blank=True, to='shop.Product_Choice'),
        ),
    ]
