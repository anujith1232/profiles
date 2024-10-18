from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["username", "bio", "skills", "contact_email", "image"]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the username'}),
            'bio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the Bio'}),
            'skills': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the Skills'}),
            'contact_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter the email'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
