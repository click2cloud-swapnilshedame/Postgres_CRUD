import public as public
from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=30)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.name

