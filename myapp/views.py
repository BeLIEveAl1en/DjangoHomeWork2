from django.shortcuts import render, get_object_or_404
from .models import Client, Product, Order


def create_client(name, email, phone_number, address):
    client = Client.objects.create(name=name, email=email, phone_number=phone_number, address=address)
    return client


def get_client(client_id):
    client = get_object_or_404(Client, id=client_id)
    return client


def update_client(client_id, **kwargs):
    client = get_object_or_404(Client, id=client_id)
    for key, value in kwargs.items():
        setattr(client, key, value)
    client.save()
    return client


def delete_client(client_id):
    client = get_object_or_404(Client, id=client_id)
    client.delete()


def create_product(name, description, price, quantity):
    product = Product.objects.create(name=name, description=description, price=price, quantity=quantity)
    return product


def get_product(product_id):
    product = get_object_or_404(Product, id=product_id)
    return product


def update_product(product_id, **kwargs):
    product = get_object_or_404(Product, id=product_id)
    for key, value in kwargs.items():
        setattr(product, key, value)
    product.save()
    return product


def delete_product(product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()


def create_order(client, products, total_amount):
    order = Order.objects.create(client=client, total_amount=total_amount)
    order.products.set(products)
    return order


def get_order(order_id):
    order = get_object_or_404(Order, id=order_id)
    return order


def update_order(order_id, **kwargs):
    order = get_object_or_404(Order, id=order_id)
    for key, value in kwargs.items():
        setattr(order, key, value)
    order.save()
    return order


def delete_order(order_id):
    order = get_object_or_404(Order, id=order_id)
    order.delete()
