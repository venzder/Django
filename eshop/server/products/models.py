from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255, unique=True)
    full_description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='media/images')
    alt = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    coast = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return self.name

