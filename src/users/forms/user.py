from django import forms
from django.contrib.auth import get_user_model
#from users.models import Profile
from django.contrib.auth.password_validation import validate_password
from django.core import validators

User = get_user_model()

class UserCreationForm(forms.ModelForm):

    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput, validators=[validate_password])
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email']

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2

class UserUpdateForm(forms.ModelForm):
    pass
    #Hacer cambio de contraseña
    #Hacer cambio de email