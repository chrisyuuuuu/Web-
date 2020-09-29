from django.db import models

# Create your models here.


class Man(models.Model):

    m_name = models.CharField(max_length=16)
    m_height= models.IntegerField(default=185)