from django.db import models

# Create your models here.
class Something(models.Model):
    value = models.BooleanField(default=False)
