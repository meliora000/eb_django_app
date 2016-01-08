from django import forms

class LoginFrom(forms.Form):
    login_id = forms.CharField(label="Your Name",max_length=100)
    login_password = forms.CharField(label="Your Password",widget=forms.PasswordInput,max_length=100)

class SignUpForm(forms.Form):
    signup_name = forms.CharField(label="",max_length=100,widget=forms.TextInput(attrs={'placeholder':'Your Name','class':'username'}))
    signup_id = forms.CharField(label="",max_length=100,widget=forms.TextInput(attrs={'placeholder':'USER ID','class':'userid'}))
    signup_email = forms.CharField(label="",max_length=100,widget=forms.TextInput(attrs={'placeholder':'Email','class':'userid'}))
    signup_password = forms.CharField(label="",widget=forms.PasswordInput(attrs={'placeholder':'Password','class':'password1'}),max_length=100)
    signup_password_doubleCheck =forms.CharField(label="",widget=forms.PasswordInput(attrs={'placeholder':'double check password','class':'password2'}),max_length=100)