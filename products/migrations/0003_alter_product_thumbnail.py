# Generated by Django 4.0.5 on 2022-06-21 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='thumbnail',
            field=models.ImageField(upload_to='uploads/%Y/%m/%d/', verbose_name='썸네일'),
        ),
    ]