# Generated by Django 3.1.5 on 2021-04-02 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20210402_1830'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment',
            field=models.CharField(blank=True, choices=[('cash', 'CASH'), ('online', 'Online Bank')], max_length=20, null=True),
        ),
    ]
