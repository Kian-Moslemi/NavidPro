from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    class  Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.name

FOOD_SIZE = (
    ('small','Small'),
    ('medium','Medium'),
    ('large','Large')
)

class Product(models.Model):
    name = models.CharField(max_length=70)
    price = models.IntegerField()
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='media/')
    size = models.CharField(choices=FOOD_SIZE,max_length=10,default='small')
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default=None)
    created = models.DateTimeField(auto_now_add=True)
    price_medium = models.IntegerField(blank=True,default=0)
    price_large = models.IntegerField(blank=True,default=0)


    def __str__(self):
        return self.name
    





