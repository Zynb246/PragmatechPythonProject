# Generated by Django 3.1.7 on 2021-03-10 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0006_auto_20210303_2134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcategory',
            name='brands',
        ),
    ]