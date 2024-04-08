from typing import Any
from django.db import models

"""
1. 커피 고르기
2. 아이스/핫, 컵 사이즈, 결제방법, 장바구니, 메뉴사진??(보류)
3. 고객 전화번호 누르면 알려줌
"""

# Create your models here.


class Menu(models.Model):
    # coffee, latte, tea, dessert 
    menu = models.CharField(max_length=200) # coffee

    def __str__(self) -> str:
        return self.menu
    

class MenuCategory(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    menu_name = models.CharField(max_length=200) # americano
    price = models.IntegerField(default=0) #3,500원 

    def __str__(self) -> str:
        return self.menu_name
    

class Customer(models.Model):
    phone_num = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.phone_num
    

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_menu = models.ForeignKey(MenuCategory, on_delete=models.CASCADE, related_name='orders', related_query_name="order") 
    count = models.IntegerField(default=0)
    order_date = models.DateField(auto_now=True)


    
