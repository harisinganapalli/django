from django.db import models

# Create your models here.
# one to one relation 
class User(models.Model):
    username=models.CharField(max_length=50)

    def __str__(self):
        return self.username

class Userprofile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    bio=models.TextField()

    def __str__(self):
        return self.user.username
    
    # one to many relation
class Department(models.Model):
        dptname=models.CharField(max_length=40)
        experience=models.CharField(max_length=20)

        def __str__(self):
            return self.dptname

class Employee(models.Model):
        name=models.CharField(max_length=40)
        age=models.CharField(max_length=3)
        department=models.ForeignKey('Department',on_delete=models.CASCADE,related_name='emp') 

        def __str__(self):
            return self.name   
        

        # many to many  

class Author(models.Model):
    name = models.CharField(max_length=100)
    

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    

    def __str__(self):
        return self.title
    

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name   
