# from django import forms
# from .models import Students

# class Student(forms.ModelForm):
#      class Meta:
#           model=Students
#           fields="__all__"


from django import forms
from .models import Book
from django.core.exceptions import ValidationError
from datetime import datetime


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"

#     def clean(self):
#         cleaned_date=super().clean()
#         date=self.cleaned_data['']
#         print(type(date))
#         print(date)
        
