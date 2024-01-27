from django.db import models

class Product(models.Model):
  product_name = models.CharField(max_length=255),
  price = models.DecimalField(max_digits=10, decimal_places=2),
  stock_quantity = models.IntegerField(),
  barcode = models.CharField(max_length=13),
  category = models.CharField(max_length=255)

  def __str__(self):
    return self.title

  class Meta:
    db_table = 'product'
    
class Customer(models.Model):
  customer_name = models.CharField(max_length=255),
  customer_email = models.CharField(max_length=255),
  customer_phone = models.CharField(max_length=255),
  customer_address = models.CharField(max_length=255),
  customer_city = models.CharField(max_length=255),
  customer_state = models.CharField(max_length=255),
  customer_zip = models.CharField(max_length=255),
  customer_country = models.CharField(max_length=255)

  def __str__(self):
    return self.title

  class Meta:
    db_table = 'customer'


class Sales(models.Model):
  sales_date = models.DateField(),
  sales_customer = models.ForeignKey(Customer, on_delete=models.CASCADE),
  sales_product = models.ForeignKey(Product, on_delete=models.CASCADE),
  sales_quantity = models.IntegerField(),
  sales_price = models.DecimalField(max_digits=10, decimal_places=2),
  sales_total = models.DecimalField(max_digits=10, decimal_places=2)

  def __str__(self):
    return self.title

  class Meta:
    db_table = 'sales'

class SalesItem(models.Model):
  sales_item_id = models.AutoField(primary_key=True),
  sales_item_sales = models.ForeignKey(Sales, on_delete=models.CASCADE),
  sales_item_product = models.ForeignKey(Product, on_delete=models.CASCADE),
  sales_item_quantity = models.IntegerField(),
  sales_item_price = models.DecimalField(max_digits=10, decimal_places=2),
  sales_item_total = models.DecimalField(max_digits=10, decimal_places=2)

  def __str__(self):
    return self.title

  class Meta:
    db_table = 'sales_item'

class User(models.Model):
  user_id = models.AutoField(primary_key=True),
  user_name = models.CharField(max_length=255),
  user_email = models.CharField(max_length=255),
  user_password = models.CharField(max_length=255),
  user_role = models.CharField(max_length=255),
  user_status = models.CharField(max_length=255),
  user_created_date = models.DateField(),

  def __str__(self):
    return self.title

  class Meta:
    db_table = 'user'

class Order(models.Model):
  order_id = models.AutoField(primary_key=True),
  customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE),
  order_date = models.DateField(),
  order_status = models.CharField(max_length=255),
  order_total = models.DecimalField(max_digits=10, decimal_places=2)
  
  def __str__(self):
    return self.title

  class Meta:
    db_model = 'order'

class OrderItem(models.Model):
  order_item_id = models.AutoField(primary_key=True),
  order_item_order = models.ForeignKey(Order, on_delete=models.CASCADE),
  order_item_product = models.ForeignKey(Product, on_delete=models.CASCADE),
  order_item_quantity = models.IntegerField(),
  order_item_price = models.DecimalField(max_digits=10, decimal_places=2),
  order_item_total = models.DecimalField(max_digits=10, decimal_places=2)

  def __str__(self):
    return self.title

  class Meta:
    db_table = 'order_item'

class Delivery(models.Model):
  delivery_id = models.AutoField(primary_key=True),
  delivery_order = models.ForeignKey(Order, on_delete=models.CASCADE),
  delivery_date = models.DateField(),
  delivery_status = models.CharField(max_length=255),
  delivery_total = models.DecimalField(max_digits=10, decimal_places=2)

  def __str__(self):
    return self.title

  class Meta:
    db_table = 'delivery'