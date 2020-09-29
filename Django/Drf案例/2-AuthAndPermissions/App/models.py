from django.contrib.auth.hashers import check_password
from django.db import models

# Create your models here.

class BlogUser(models.Model):
    b_username = models.CharField(max_length=32)
    b_password = models.CharField(max_length=256)

    def verify_password(self, password):
        return check_password(password, self.b_password)


class Blog(models.Model):
    b_title = models.CharField(max_length=32)
    b_content = models.CharField(max_length=256)
    b_user = models.ForeignKey(BlogUser)