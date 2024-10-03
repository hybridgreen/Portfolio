from django import forms

class Contact_form(forms.Form):
    name = forms.CharField(max_length=50, label="Name", required= True)
    email = forms.EmailField(label="Email", required= True)
    number = forms.CharField(max_length=50, label= "Phone", required=False)
    subject = forms.CharField(max_length=100)
    message = forms.CharField(max_length=1000, widget=forms.Textarea)
