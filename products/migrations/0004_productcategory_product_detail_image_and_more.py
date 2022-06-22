# Generated by Django 4.0.5 on 2022-06-22 00:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_thumbnail'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='상품카테고리')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='detail_image',
            field=models.FileField(default='', upload_to='uploads/detail/%Y/%m/%d/', verbose_name=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='thumbnail',
            field=models.FileField(upload_to='uploads/thumbnail/%Y/%m/%d/', verbose_name=''),
        ),
        migrations.CreateModel(
            name='ProductOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='상품옵션')),
                ('price', models.IntegerField(verbose_name='상품가격')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='상품')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='product_categoy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.productcategory', verbose_name='카테고리'),
        ),
    ]