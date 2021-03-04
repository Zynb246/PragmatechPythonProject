# Generated by Django 3.1.7 on 2021-03-03 17:34

import django.core.files.storage
from django.db import migrations, models
import product.models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auto_20210302_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='C:\\Users\\admın\\Desktop\\progmatech_project\\PragmatechPythonProject-master\\ecommerce\\media'), upload_to=product.models.upload_product_file_loc),
        ),
        migrations.AlterField(
            model_name='productfile',
            name='file',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location='C:\\Users\\admın\\Desktop\\progmatech_project\\PragmatechPythonProject-master\\static_cdn\\product_media'), upload_to=product.models.upload_product_file_loc),
        ),
    ]
