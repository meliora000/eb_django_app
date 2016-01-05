from django import forms

class LoginFrom(forms.Form):
    login_id = forms.CharField(label="Your Name",max_length=100)
    login_password = forms.CharField(label="Your Password",widget=forms.PasswordInput,max_length=100)

class SignUpForm(forms.Form):
    signup_name = forms.CharField(label="Your Name",max_length=100)
    signup_id = forms.CharField(label="Your ID",max_length=100)
    signup_email = forms.CharField(label="Your Email",max_length=100)
    signup_password = forms.CharField(label="Your Password",widget=forms.PasswordInput,max_length=100)
    signup_password_doubleCheck = forms.CharField(label="Check Password",widget=forms.PasswordInput,max_length=100)