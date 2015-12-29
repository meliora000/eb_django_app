from django import forms

class LoginFrom(forms.Form):
    login_id = forms.CharField(label="Your Name",max_length=100)
    login_password = forms.CharField(label="Your Password",widget=forms.PasswordInput,max_length=100)
