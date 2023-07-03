from django.contrib.auth.forms import forms, User, UserCreationForm, AuthenticationForm

class UserRegisterForm(UserCreationForm):
    
     username = forms.CharField(
         label = 'Nombre de Usuario',
         required=True,
     )
     password1 = forms.CharField(
         label = "Contraseña",
         required=True
     )
     password2 = forms.CharField(
         label = "Confirmar Contraseña",
         required=True
    )
class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']