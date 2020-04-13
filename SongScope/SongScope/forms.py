from django import forms


class RawProductForm(forms.Form):
    userInput = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'class': 'form-control form-control-light w-100',
            'type': "text",
            'placeholder': "Search",
        }
    ))


class SongSelectionForm(forms.Form):
    artist = forms.CharField(widget=forms.HiddenInput(), required=False)
    track = forms.CharField(widget=forms.HiddenInput(), required=False)
    songSelection = forms.CharField(widget=forms.HiddenInput(), required=False)
    albumSelection = forms.CharField(widget=forms.HiddenInput(), required=False)
    userInput = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'class': 'form-control form-control-light w-100',
            'type': "text",
            'placeholder': "Search",
        }
    ))


