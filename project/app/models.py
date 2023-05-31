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
    
class new(models.Model):
     name=models.CharField(max_length=23)
     company=models.CharField(max_length=50)

# class Postion(models.Model):
#     title=models.CharField(max_length=55)


# class employee(models.Model):
#     fullname=models.CharField(max_length=50)
#     employeecode=models.CharField(max_length=5)
#     number=models.CharField(max_length=15)
#     position=models.ForeignKey(Postion,on_delete=models.CASCADE)

         