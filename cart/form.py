from django import forms 

QUANTITY = [(i, str(i)) for i in range(1, 20)]

class CartAddForm(forms.Form):
    quantity = forms.TypedChoiceField(
        choices=QUANTITY,label="Quantidade", coerce=int
    )
    override = forms.BooleanField(
        required=False, initial=False, widget=forms.HiddenInput
    )
