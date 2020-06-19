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


class Review(models.Model):
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='products')
    author = models.CharField(max_length=200)
    review = models.TextField()
    created_date = models.DateTimeField(auto_now=True)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.review
