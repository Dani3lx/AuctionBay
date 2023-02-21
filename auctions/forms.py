from django import forms
from .models import Listing

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ('listing_name', 'listing_desc', 'starting_bid', 'picture')

        widgets = {
            'listing_name': forms.TextInput(attrs={'class' : 'form-control', 'maxlength' : "64"}),
            'listing_desc': forms.TextInput(attrs={'class' : 'form-control', 'maxlength' : "256"}),
            'starting_bid': forms.NumberInput(attrs={'class' : 'form-control'}),
        }

