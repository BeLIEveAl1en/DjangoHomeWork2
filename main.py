from django.db import models
from django.utils import timezone


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    registration_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    added_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Order #{self.pk} - {self.client.name}"

    def calculate_total_amount(self):
        total = 0
        for product in self.products.all():
            total += product.price * product.quantity
        self.total_amount = total
        self.save()

    def add_product(self, product, quantity):
        self.products.add(product)
        self.calculate_total_amount()

    def remove_product(self, product):
        self.products.remove(product)
        self.calculate_total_amount()
