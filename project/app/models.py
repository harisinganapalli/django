from django.db import models

# Create your models here.
class  classes(models.Model):
    firstname=models.CharField(max_length=60)
    lastname=models.CharField(max_length=100)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True) 
    age=models.IntegerField(null=True)

    def __str__ (self):
      return f"{self.firstname} {self.lastname}"   