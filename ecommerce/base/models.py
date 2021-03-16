from django.db import models

# Create your models here.
class Wishlist(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=None)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    
def __str__(self):
    return str(self.id)