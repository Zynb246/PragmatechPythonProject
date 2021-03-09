from django.db import models

# Create your models here.

class Slider(models.Model):
    url =  models.URLField(max_length=200)
    image = models.ImageField(upload_to='slider', height_field=None, width_field=None, max_length=100)


    def __str__(self):
        return self.url