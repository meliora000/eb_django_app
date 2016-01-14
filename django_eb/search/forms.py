from django import forms

class LoginFrom(forms.Form):
    login_id = forms.CharField(label="",max_length=100,widget=forms.TextInput(attrs={'placeholder':'User ID'}))
    login_password = forms.CharField(label="",widget=forms.PasswordInput(attrs={'placeholder':'Password'}),max_length=100)

class CommentForm(forms.Form):
    login_id = forms.CharField(label="",max_length=500,widget=forms.Textarea(attrs={'placeholder':'Comment','id':'comment_form','name':'user_comment'}))