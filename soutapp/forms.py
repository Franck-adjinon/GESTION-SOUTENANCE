from django import forms  

class MessageForm(forms.Form):
    sujet = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control', 
        'placeholder': 'Sujet'
    }))
    email_user = forms.CharField(max_length=255, widget=forms.TextInput(attrs={
        'class': 'form-control', 
        'placeholder': 'Votre Email'
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'id': 'message',
        'rows': 7,
        'cols': 30,
        'placeholder': 'Message'
    }))