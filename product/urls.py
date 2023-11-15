from django.urls import path
from .import views

urlpatterns = [
    path("user/",views.user_list,name='user'),
    path("product/",views.product_list,name='product'),
 ]