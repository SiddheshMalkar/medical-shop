from django.db import models

# Create your models here.


class Customer(models.Model):
    customerid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Medicine(models.Model):
    mid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.name

'''class Stock(models.Model):
    sid = models.AutoField(primary_key=True)
    mid = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    quantity = models.IntegerField()'''