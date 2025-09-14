from django.db import models
from django.contrib.auth.models import User

class Address(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="address")
    title = models.CharField(max_length=50)
    address_line = models.TextField()

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'

    def __str__(self):
        return f'{self.title} - {self.address_line[:15]}'


class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    address = models.ForeignKey(Address,on_delete=models.SET_NULL,null=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    postal_code = models.CharField(max_length=40,unique=True)
    phone = models.CharField(max_length=14)
    email = models.EmailField()

    def __str__(self):
        return f'{self.last_name} - {self.postal_code}'

