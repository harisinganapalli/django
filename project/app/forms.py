from django import forms
from .models import employee 

POSITIONS= [
     ('select','Select'),
    ('manager', 'Manager'),
    ('ceo', 'CEO'),
    ('assit.manager','Assit.manager'),
    ('hr','HR'),
    ('director','Director') 
    ]

class Employeeform(forms.ModelForm):
     position= forms.CharField(label='position', widget=forms.Select(choices=POSITIONS))

     class Meta:
          model= employee  
          fields= {'fullname','employeecode','number','position'}
          labels ={
               'fullname':'Full Name',
               'employeecode':'Employee Code ',
               'number':'Number',
               'position':'Position'
          }

     # def __init__(self):
     #      self.fields['employeecode'].required=False      