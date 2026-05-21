# from itertools import product
#
#
# class Product:
#     def __init__(self,name,price,quantity):
#         self.name=name
#         self.price=price
#         self.quantity=quantity
# class Cart:
#     def __init__(self,product):
#         self.cart=cart
#     def __add__(self, other):
#         self.product.append(product)
#         reutrn self
#     def __sub__(self, product):
#         if self
#         self.other.remove(product)
# class BankAccount:
#
#     def __init__(self, holder, balance):
#         self.account_holder = holder
#         self.balance = balance
#
#     def deposit(self, amount):
#         self.balance += amount
#
#     def withdraw(self, amount):
#         self.balance -= amount
#
#     def __str__(self):
#         return f"{self.account_holder} : {self.balance}"
#
#     def __add__(self, other):
#         return self.balance + other.balance
#
#     def __sub__(self, other):
#         return self.balance - other.balance
#
#     def __eq__(self, other):
#         return self.balance == other.balance
#
#     def __lt__(self, other):
#         return self.balance < other.balance
#
#     def __getattribute__(self, name):
#         print(f"Accessing {name}")
#         return object.__getattribute__(self, name)
#
#     def __setattr__(self, name, value):
#         if name == "balance" and value < 0:
#             print("Negative balance not allowed")
#         else:
#             object.__setattr__(self, name, value)
#
#
# a1 = BankAccount("Razaq", 5000)
# a2 = BankAccount("Ali", 3000)
#
# print(a1)
# print(a1 + a2)
# print(a1 - a2)
# print(a1 == a2)
# print(a1 < a2)
#
#
#
#
# class Product:
#
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#
#     def total_price(self):
#         return self.price * self.quantity
#
#     def __str__(self):
#         return f"{self.name} - {self.price}"
#
#     def __add__(self, other):
#         return self.total_price() + other.total_price()
#
#     def __mul__(self, num):
#         return self.price * num
#
#     def __gt__(self, other):
#         return self.total_price() > other.total_price()
#
#     def __eq__(self, other):
#         return self.price == other.price
#
#     def __getattr__(self, name):
#         return "Attribute not found"
#
#     def __setattr__(self, name, value):
#         if name == "price" and value < 0:
#             print("Invalid price")
#         else:
#             object.__setattr__(self, name, value)
#
#
# p1 = Product("Laptop", 50000, 2)
# p2 = Product("Phone", 30000, 1)
#
# print(p1 + p2)
# print(p1 * 2)
# print(p1 > p2)
# class A:
#     def m1(self):
#         print("class")
# class B:
#     def m1(self):
#         print("B")
#         super().m1()
# class C:
#     def m1(self):
#         print("C")
#         super().m1()
# class D(A,B,C):
#     def m1(self):
#         print("D")
#         super().m1()
# d1=D()
# d1.m1()
# print(D.mro())
#
