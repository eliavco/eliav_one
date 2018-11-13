from django import forms

def valid_z(word):
    if word[0].lower() != 'z':
        raise forms.ValidationError(
            ("Accidentally enterd something starting with a  %(value)s instead of a 'z'"),
            params={'value': word[0]},
        )

class Survey(forms.Form):
    name = forms.CharField(max_length=30,validators=[valid_z])
    opinion = forms.CharField(max_length=300)
