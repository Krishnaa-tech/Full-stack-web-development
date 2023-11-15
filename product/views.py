from django.shortcuts import render
from .models import User, Product


# View to insert user data and display a list of users
def user_list(request):
    user_data = [
        {"name": "Reuben", "phone_no": "7895835489", "city": "Pune", "state": "Maharashtra"},
        {"name": "Salomi", "phone_no": "7895835410", "city": "Mumbai", "state": "Maharashtra"},
        {"name": "Titus", "phone_no": "7895837892", "city": "Bangalore", "state": "Karnataka"},
    ]
    for data in user_data:
        user = User(**data)
        user.save()
    users = User.objects.all()
    return render(request, 'product.html', context={'users': users})

# View to insert product data and display a list of products
def product_list(request):
    product_data = [
    {"userid": User.objects.get(userid=1), "product_id": 10120, "product_name": "Nike shoes", "product_cost": 5865, "category": "Shoes", "quantity": 1, "image_path":"images/img1.jpeg"},
    {"userid": User.objects.get(userid=1), "product_id": 10121, "product_name": "John Players Jeans", "product_cost": 1499, "category": "Jeans", "quantity": 2, "image_path":"images/img2.jpeg"},
    {"userid": User.objects.get(userid=2), "product_id": 10123, "product_name": "Dillinger T-shirt", "product_cost": 1199, "category": "T-shirts", "quantity": 2, "image_path":"images/img3.jpeg"},
    {"userid": User.objects.get(userid=2), "product_id": 10124, "product_name": "Baggit tote bag", "product_cost": 2090, "category": "Bags", "quantity": 1, "image_path":"images/img4.jpeg"},
    {"userid": User.objects.get(userid=3), "product_id": 10125, "product_name": "Fossil Men watch", "product_cost": 14495, "category": "Watches", "quantity": 1, "image_path":"images/img5.jpeg"},
    {"userid": User.objects.get(userid=1), "product_id": 10126, "product_name": "Lenovo Laptop", "product_cost": 70000, "category": "Computers", "quantity": 1, "image_path":"images/img6.jpeg"},
    {"userid": User.objects.get(userid=3), "product_id": 10127, "product_name": "Dell Laptop", "product_cost": 85000, "category": "Computers", "quantity": 1,  "image_path":"images/img7.jpeg"},
    {"userid": User.objects.get(userid=1), "product_id": 10128, "product_name": "Biscuits", "product_cost": 200, "category": "Grocerys", "quantity": 1 , "image_path":"images/img8.jpeg"},
    {"userid": User.objects.get(userid=2), "product_id": 10129, "product_name": "Mercedez", "product_cost": 2000000, "category": "Cars", "quantity": 1, "image_path":"images/img9.jpeg"},
    {"userid": User.objects.get(userid=3), "product_id": 10130, "product_name": "Alto-800", "product_cost": 500000, "category": "Cars", "quantity": 1, "image_path":"images/img10.jpeg"},
    ]
    
    # Insert data into the "product" table
    for data in product_data:
        product = Product(**data)
        product.save()
    
    products = Product.objects.all()
    return render(request, 'product.html', context={'products': products})
