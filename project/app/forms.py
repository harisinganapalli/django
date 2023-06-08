from django import forms
from .models import Students,employee
from django.forms.widgets import NumberInput 
from django.core.exceptions import ValidationError

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

Choice = [('1', 'Male'), ('2', '  Female'), ('3', 'Others')]
class Student(forms.ModelForm):
     date_of_birth = forms.DateField(widget = NumberInput(attrs={'type':'date'})) 
     rank = forms.ChoiceField(widget = forms.RadioSelect, choices=Choice)  

     class Meta:
          model=Students
          fields="__all__"
     def clean(self):
          cleaned_data=super().clean()
          f = self.cleaned_data['firstname'] 
          r=self.cleaned_data['lastname']
          h=self.cleaned_data['phonenumber']
          if len(f) <= 5:
               raise forms.ValidationError("firstname have more than 5 values ")
          
          if len(r)<= 6:
               raise forms.ValidationError("lastname have more than 6 values") 

          if len(h)<10:
               raise forms.ValidationError('phone number must be in 10 digits')  
