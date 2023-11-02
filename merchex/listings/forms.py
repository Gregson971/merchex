from django import forms

from listings.models import Band, Listing


class ContactUsForm(forms.Form):
    name = forms.CharField(required=False, max_length=100)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True, max_length=5000)


class BandForm(forms.ModelForm):
    class Meta:
        model = Band
        fields = '__all__'


class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = '__all__'
