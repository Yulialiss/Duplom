from django import forms

class CardPaymentForm(forms.Form):
    card_number = forms.CharField(max_length=16, widget=forms.TextInput(attrs={'placeholder': 'Card Number'}))
    card_holder = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Card Holder Name'}))
    amount = forms.DecimalField(max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={'placeholder': 'Amount'}))
