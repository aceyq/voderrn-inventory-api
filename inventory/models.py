from django.db import models
import uuid #create unique product IDs

class User(models.Model):
    USER_TYPES = [
        ("customer", "Customer"),
        ("seller", "Seller"),
        ("admin", "Admin"),
    ] #list of allowed roles (dropdown menu)

    user_id = models.AutoField(primary_key = True) #creates ID number, sets as primary key
    user_name = models.CharField(max_length=100) #creates username, up to 100 chars
    user_type = models.CharField(max_length=10, choices = USER_TYPES, default = 'customer')
    #text field with restricted choices, only customer/seller/admin
    #if not specified, defaults to "customer"

    def __str__(self):
        return f"{self.user_name} ({self.user_type})"
        #instead of "User object(3)", it will say "Acelynn (admin)"

class Category(models.Model):
    category_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 100)
    description = models.TextField()
    #Store the name of the category and a longer text description 

    def __str__(self):
        return self.name 

class Product(models.Model):
    #creates a table for products like "Yoga Mat"
    product_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable = False)
    #UUID is a long unique ID like b12... more secure than just using numbers
    name = models.CharField(max_length = 100)
    description = models.TextField()
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    #store prices like 12.99, decimal places are for cents
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    #created_at saved once when the product is created
    #updated_at auto-updates every time the product is edited

    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    #links this product to a user (seller who added it)
    #on_delete: if a seller is deleted, their products are deleted too

    def __str__(self):
        return self.name





