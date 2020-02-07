from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    messsage = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
    