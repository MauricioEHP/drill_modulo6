from django import forms
from .models import VehiculoModel
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class VehiculoForm(forms.ModelForm):
    class Meta:
        model = VehiculoModel
        fields = "__all__"

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required= True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(RegistroUsuarioForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    
class RegistroUsuarioForm2(forms.ModelForm):
    # Agrega un campo para seleccionar el tipo de usuario
    TIPO_USUARIO_CHOICES = (
        ('Gvisualizar', 'Usuario'),
        ('ver_addgrupo', 'Avanzado'),
        ('staff', 'Miembro del Staff'),
    )
    tipo_usuario = forms.ChoiceField(choices=TIPO_USUARIO_CHOICES)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'tipo_usuario')
        widgets = {
            'password': forms.PasswordInput(),
        }