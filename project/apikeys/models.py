from django.db import models

# Create your models here.
# crud in class based
class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name
