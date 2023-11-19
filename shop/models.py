from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse



class Catog(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('prod_ct', args=[self.slug])

    def __str__(self):
        return self.name

class Products(models.Model):
    category = models.ForeignKey(Catog, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    img = models.ImageField(upload_to='products')
    desc = models.TextField()
    stock = models.IntegerField()
    available = models.BooleanField()
    price = models.IntegerField()

    def get_url(self):
        return reverse ('details',args=[self.category.slug,self.slug])
    

    def __str__(self):
        return self.name

