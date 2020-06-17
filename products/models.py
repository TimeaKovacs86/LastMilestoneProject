from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=254, default="")
    description_section = models.TextField(default="")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    currency = models.CharField(max_length=1, default='€')
    images = models.ImageField(upload_to="images", blank=True)
    slug = models.SlugField(max_length=50, default="")

    def __str__(self):
        return self.name

    def snippet(self):
        return self.description_section[:120] + "..."

