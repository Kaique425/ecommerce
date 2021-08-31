from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField


class Product (models.Model):
    name = models.CharField(max_length=64)
    slug = AutoSlugField(unique=True, always_update=False, populate_from="name")
    product_image = models.ImageField(upload_to= 'products/images',blank=True,null=True)
    price = models.DecimalField(max_digits=999, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["is_available"]

    def get_absolute_url(self):
        return reverse('product:detail', kwargs={'slug':self.slug})