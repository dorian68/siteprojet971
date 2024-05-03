from django.db import models

# Create your models here.

class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    restaurant_id = models.IntegerField()
    price = models.DecimalField(decimal_places=2,max_digits=10)
    rate = models.DecimalField(decimal_places=2,max_digits=10)
    image = models.CharField(max_length=200)

class Order(models.Model):
    Order_id = models.AutoField(primary_key=True)
    OrderNumber = models.IntegerField()
    ListArticle = list()
    OrderDate = models.DateTimeField()
    ClientAddress = models.CharField(max_length=200)
    TotalOrderPrice = models.FloatField()

