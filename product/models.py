from django.db import models

# User model
class User(models.Model):
    userid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone_no = models.CharField(max_length=15, default=0)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Product model
class Product(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255)
    product_cost = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=255)
    quantity = models.IntegerField()
    image_path=models.CharField(max_length=255)

    def __str__(self):
        return self.product_name
