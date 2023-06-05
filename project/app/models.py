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

class Postion(models.Model):
    title=models.CharField(max_length=55)
    def __str__ (self):
      return f"{self.title}"   



class employee(models.Model):
    fullname=models.CharField( max_length=100)
    employeecode=models.CharField(max_length=5,blank=True,)
    number=models.CharField(max_length=15)
    position=models.CharField(max_length=234)


    def __str__(self):
        return self.fullname
    
class Students(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    email=models.EmailField(max_length=70)
    branch=models.CharField(max_length=50)
    phonenumber=models.CharField(max_length=10)
    rollnumber=models.CharField(max_length=50)
    
    
     

    def __str__(self):
        return self.firstname   

         