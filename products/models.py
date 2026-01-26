from django.db import models

# Create your models here.
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=254, unique=True)
    friendly_name = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name if self.friendly_name else self.name