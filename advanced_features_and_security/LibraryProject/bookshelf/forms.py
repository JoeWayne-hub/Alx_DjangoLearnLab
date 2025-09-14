from django import forms

class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label="Your Name")
    email = forms.EmailField(required=True, label="Email Address")
    message = forms.CharField(
        widget=forms.Textarea,
        required=True,
        label="Message"
    )
