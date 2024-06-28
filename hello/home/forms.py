# cart/forms.py

from django import forms

class AddToCartForm(forms.Form):
    name = forms.CharField(widget=forms.HiddenInput)
    price = forms.DecimalField(widget=forms.HiddenInput)
