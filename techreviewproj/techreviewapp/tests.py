from django.test import TestCase
from .models import Product, TechType, Review
from django.urls import reverse
from django.contrib.auth.models import User

# Create your tests here.
# Tests for models.py
class TechTypeTest(TestCase):
    def test_string(self):
        type=TechType(techtypename="laptop")
        self.assertEqual(str(type), type.techtypename)

    def test_table(self):
        self.assertEqual(str(TechType._meta.db_table), 'techtype')    

class ProductTest(TestCase):
    def setUp(self):
        self.type = TechType(techtypename = 'tablet')
        self.prod = (Product(productname = 'Ipad', producttype = self.type, productprice = '800.00'))

    def test_string(self):

        self.assertEqual(str(self.prod), self. prod.productname)  

    def test_type(self):
        self.assertEqual(str(self.prod.producttype), 'tablet')   

    def test_discount(self):
        self.assertEqual(self.prod.memberDiscount(), 40.00)    

# Tests for views

class IndexTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

class GetProductsTest(TestCase):
    def setUp(self):
        self.u=User.objects.create(username='myuser')
        self.type=TechType.objects.create(techtypename='laptop')
        self.prod = Product.objects.create(productname='product1', 
        producttype=self.type, user=self.u, productprice=500.00, 
        productentrydate='2019-04-02', productdescription="a product")

    def test_product_detail_success(self):
        response = self.client.get(reverse('productdetail', args=(self.prod.id,)))
        self.assertEqual(response.status_code, 200)    
