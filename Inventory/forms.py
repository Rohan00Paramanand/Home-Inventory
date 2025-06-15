from django import forms
from .models import Item

class AddItem(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'spot', 'location']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter name of item', 'class': 'form-control'}),
            'spot': forms.TextInput(attrs={'placeholder': 'Enter where the item is kept', 'class': 'form-control'}),
            'location': forms.Select(attrs={'class': 'form-select'})
        }

class FindItem(forms.Form):
    name = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Enter name of item', 'class': 'form-control'}))
    spot = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Enter where the item is kept', 'class': 'form-control'}))
    location = forms.ChoiceField(choices=[('', 'Any')] + list(Item.ROOMS), required=False, widget=forms.Select(attrs={'class': 'form-select'}))
    start_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    end_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))