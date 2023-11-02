from django import forms


class ContactUsForm(forms.Form):
    name = forms.CharField(required=False, max_length=100)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True, max_length=5000)
