from django.db import models
from ecommerceapp.models import Product

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=250, blank=True)
    last_name = models.CharField(max_length=250, blank=True)
    username = models.CharField(max_length=250, blank=True)
    password1 = models.CharField(max_length=250, blank=True)
    email = models.CharField(max_length=250, blank=True)

    class Meta:
        db_table='User'

    def __str__(self):
        return self.username


from django.db import models

# Create your models here.
