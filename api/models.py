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
    #code 
    price = models.DecimalField(
        max_digits = 20,
        decimal_places = 2
    )

    quantity = models.IntegerField(
    )

    def __str__(self):
        return f"{self.name}"