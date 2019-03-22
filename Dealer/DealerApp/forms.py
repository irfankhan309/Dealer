from django import forms
from DealerApp.models import PostEnquiry

class PostForm(forms.ModelForm):
    class Meta:
        model=PostEnquiry
        fields= '__all__'
