"""Forms of the project."""

# Create your forms here.
from django import forms

class ThingForm(forms.Form):
    name = forms.CharField(label='Name', max_length=30, required=True)
    description = forms.CharField(label='Description', widget=forms.Textarea, max_length=120, required=False)
    quantity = forms.IntegerField(label='Quantity', widget=forms.NumberInput, min_value=0, max_value=100)