from django.db import models
from django.urls import reverse
# from django.contrib.auth.models import User

class Category(models.Model) :
   name = models.CharField(max_length=200, unique=True)
   slug = models.SlugField(max_length=100, unique=True)
   
   class Meta :
       ordering = ('name',)
       verbose_name = 'category'
       verbose_name_plural = 'categories'
       
   def __str__(self) :
       return self.name
    
class Product(models.Model) :
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200 , unique=True)
    image = models.ImageField(upload_to="Products_img")
    description = models.TextField(max_length=500 , blank=True , null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    published_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta :
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'
        
    def get_url(self) :
        return reverse('product_detail' , args=[self.slug])
        
    def __str__(self) :
        return self.name
    

class Cart (models.Model) :
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)
    class Meta :
        db_table = 'Cart'
        ordering = ['date_added']
        
    def __str__(self) :
        return self.cart_id
        
class CartItem (models.Model) :
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)
    
    class Meta :
        db_table = 'CartItem'
        
    def sub_total(self) :
        return self.product.price * self.quantity
    
    def __str__(self) :
        return self.product
        
        
    
        
    
    