from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Item(models.Model):
    category = models.ForeignKey(Category, related_name='item', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    discription = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='item_image', blank=True, null=True)
    price = models.FloatField()
    is_sold = models.BooleanField(default=False)
    create_by = models.ForeignKey(User, related_name='item', on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Items'

    def __str__(self):
        return self.name
