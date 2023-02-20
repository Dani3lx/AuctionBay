from django import forms
from .models import Listing

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ('listing_name', 'listing_desc', 'starting_bid')

        widgets = {
            'listing_name': forms.TextInput(attrs={'class' : 'form-control'}),
            'listing_desc': forms.TextInput(attrs={'class' : 'form-control'}),
            'starting_bid': forms.NumberInput(attrs={'class' : 'form-control'}),
        }

