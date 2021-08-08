from django.db import models

# Create your models here.

class Product (models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=999, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["is_available"]