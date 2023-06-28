from django import forms

from .models import BlogPost, Profile 


class ProfileForm (forms.ModelForm):
    class Meta:
        model=Profile
        # fields=('phone_no','bio','facebook','instagram','linkedin','image')
        fields='__all__'

class BlogPostForm(forms.ModelForm):
    class Meta:
        model=BlogPost
        fields=('title','slug','content','image')

    # def clean(self):
    #     cleaned_data=super().clean()
    #     a=self.cleaned_data['slug']

              
