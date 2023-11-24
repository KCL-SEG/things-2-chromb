"""Forms of the project."""
from django import forms
# Create your forms here.


class ThingForm(forms.Form):
    """Form for the Thing model."""

    name = forms.CharField(label='Name', max_length=100)
    description = forms.Textarea()
    quantity = forms.NumberInput()

