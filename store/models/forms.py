from django.forms.widgets import RadioSelect
from .Customer import User
from django import forms
from django.contrib.auth.hashers import make_password, check_password

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),

            'last_name': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),

            'email': forms.EmailInput(attrs={'class': 'form-control form-control-sm'}),

            'password': forms.PasswordInput(attrs={'class': 'form-control form-control-sm'})
        }
    
    def clean_first_name(self):
        data = self.cleaned_data.get('first_name')
        if len(data) < 4:
            raise forms.ValidationError('Bitch get me atleast 4 characters')

        return data
    
    def clean_email(self):
        data = self.cleaned_data.get('email')
        if User.objects.filter(email = data):
            raise forms.ValidationError('Email is already in USE.')
        
        return data
    
    def clean_password(self):
        data = make_password(self.cleaned_data.get('password'))
        return data


class LoginForm(forms.Form):
    email = forms.CharField(max_length=50, widget=forms.EmailInput(attrs={'class': 'form-control form-control-sm'}))
    password = forms.CharField(min_length=6, max_length=16, widget=forms.PasswordInput(attrs={'class': 'form-control form-control-sm'}))

    def is_valid(self):
 
        # run the parent validation first
        valid = super(LoginForm, self).is_valid()
    
        # so far so good, get this user based on the email
        customer = User.get_customer(self.cleaned_data['email'])

        if not customer:
            return False 

        if customer:
            flag = check_password(self.cleaned_data['password'], customer.password)
            if not flag:
                return False

        # Shit gone south
        return True