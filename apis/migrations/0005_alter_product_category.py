# Generated by Django 3.2.6 on 2021-08-07 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0004_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(max_length=20, verbose_name='category'),
        ),
    ]
