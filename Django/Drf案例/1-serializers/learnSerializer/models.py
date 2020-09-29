from django.db import models

# Create your models here.

class Blog(models.Model):
    b_title = models.CharField(max_length=32)
    b_content = models.CharField(max_length=256)

class Goods(models.Model):
    g_name = models.CharField(max_length=32)
    g_price = models.FloatField(default=1)