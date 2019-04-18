from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TechType(models.Model):
    techtypename=models.CharField(max_length=255)
    techdescription=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.techtypename

    class Meta:
        db_table='techtype'
        verbose_name_plural='techtypes'    

class Product(models.Model):
    productname=models.CharField(max_length=255)
    producttype=models.ForeignKey(TechType, on_delete=models.DO_NOTHING)
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    productprice=models.DecimalField(max_digits=10, decimal_places=2)
    productentrydate=models.DateField()
    producturl=models.URLField(null=True, blank=True)
    productdescription=models.TextField(null=True, blank=True)

    #returns the amount of discount for members
    def memberDiscount(self):
        discount=.05
        return float(self.productprice) * discount

    #returns the discounted price for members
    def discountedPrice(self):
        discount=self.memberDiscount()
        return float(self.productprice) - discount    

    def __str__(self):
        return self.productname

    class Meta:
        db_table='product'
        verbose_name_plural='products' 

class Review(models.Model):
    reviewtitle=models.CharField(max_length=255)
    reviewdate=models.DateField()
    product=models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    user=models.ManyToManyField(User)
    rating=models.SmallIntegerField()
    reviewtext=models.TextField()


    def __str__(self):
        return self.reviewtitle

    class Meta:
        db_table='review'
        verbose_name_plural='reviews'