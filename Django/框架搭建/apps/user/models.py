from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from db.base_model import BaseModel


class User(AbstractUser,BaseModel):
    '''用户模型类'''
    class Meta:
        db_table = 'user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        ordering = ('last_login',)

