# Generated by Django 3.1.7 on 2021-03-10 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Staticpage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='image',
            field=models.ImageField(upload_to='slider'),
        ),
    ]