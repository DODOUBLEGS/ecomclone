# Generated by Django 5.0.1 on 2024-01-19 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_shop_category_shop_categories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='product',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='products',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='user',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
        migrations.DeleteModel(
            name='Wishlist',
        ),
    ]
