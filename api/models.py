from django.db import models

# Create your models here.

class Product(models.Model):

    name = models.CharField(
        max_length=50, 
        default=None, 
        blank=True, 
        unique=True, 
        verbose_name="Product Name", 
        help_text="The name of the product"
    ) 
    price = models.DecimalField(
        max_digits = 20,
        decimal_places = 2,
        default=None, 
        blank=True, 
    )
    quantity = models.IntegerField(
        default=None, 
        blank=True, 
        null=True,
    )
    images = models.ImageField(
        upload_to="files/images/product",
        null=True,
    )

    def __str__(self):
        return f"{self.name}"