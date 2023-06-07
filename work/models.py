from django.db import models

class Book(models.Model):
    FirstName = models.CharField(max_length=200)
    LastName = models.CharField(max_length=100)
    Date_of_Dirth = models.DateField()
    Email=models.EmailField( null=True)
    PhoneNumber=models.CharField(null=True,max_length=10)

    class Meta:
        db_table = "books"
     
    def __str__(self):
        return self.FirstName
       