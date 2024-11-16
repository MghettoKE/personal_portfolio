from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    phone_number = forms.CharField(max_length=15, required=False, widget=forms.TextInput(attrs={'placeholder': 'Your phone number'}))

    class Meta:
        model = Contact
        fields = ['name', 'email','phone_number', 'message']
        widgets = {'name': forms.TextInput(attrs={'placeholder': 'your name'}),
                   'email': forms.TextInput(attrs={'placeholder': 'your email'}),
                   'message': forms.Textarea(attrs={'placeholder': 'your message'}),
                   }