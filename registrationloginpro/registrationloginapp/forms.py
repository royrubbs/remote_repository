from django import forms

class RegistrationForm(forms.Form):
    name=forms.CharField(
        label="Enter name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Name',
            }
        )
    )
    password1=forms.CharField(
        label="Enter password1",
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'password1',
            }
        )
    )
    email=forms.CharField(
        label="Enter email id",
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'email id',
            }
        )
    )
    mobile=forms.CharField(
        label=" Your mobile",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'mobile num',
            }
        )
    )

class LoginForm(forms.Form):
    email = forms.EmailField(
        label="Enter email",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'email',
            }
        )
    )
    password1 = forms.CharField(
        label="Enter password1",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'password1',
            }
        )
    )
