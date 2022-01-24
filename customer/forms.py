from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)


class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    first_name = forms.CharField(widget=forms.TextInput, required=True)
    last_name = forms.CharField(widget=forms.TextInput, required=True)
