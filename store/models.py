from django.db import models
from tinymce.models import HTMLField

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    name_uz = models.CharField(max_length=200, null=True)
    name_ru = models.CharField(max_length=200, null=True)

    title = models.CharField(max_length=200, null=True)
    title_ru = models.CharField(max_length=200, null=True)
    title_uz = models.CharField(max_length=200, null=True)

    description_ru = models.TextField()
    description_uz = models.TextField()
    description = models.TextField()
    line_ru = HTMLField()
    line_uz = HTMLField()
    line = HTMLField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    digital = models.BooleanField(default=False, null=True, blank=True)
    image = models.ImageField(default="default.jpg", upload_to='static/db/products/')

    def __str__(self):
        return self.name

    @property
    def product_url(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
   

class Order(models.Model):
    date_ordered = models.DateTimeField(auto_now_add=True)
    city = models.CharField(max_length=100, default='Tashkent')
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    @property
    def get_cart_total(self):
        order_items = self.orderitem_set.all()
        total = sum([item.get_total for item in order_items])
        return total

    @property
    def get_cart_items(self):
        order_items = self.orderitem_set.all()
        total = sum([item.quantity for item in order_items])
        return total

    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_ended = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        if self.product:
            total = self.product.price * self.quantity
        else:
            total = 0
        return total

    def __str__(self):
        return self.product.name
