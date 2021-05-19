# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.forms import AuthenticationForm
from django import forms
from usuario.models import Usuario

class RegistroForm(forms.ModelForm):

    password1 = forms.CharField(label= 'Contraseña', widget= forms.PasswordInput(
        attrs= {
            'class': 'form-control',
            'placeholder' : 'Ingrese su contraseña...',
            'id' : 'password1',
            'required' : 'required',
        }
    ))

    password2 = forms.CharField(label= 'Contraseña de confirmación', widget= forms.PasswordInput(
        attrs= {
            'class': 'form-control',
            'placeholder' : 'Ingrese nuevamente su contraseña...',
            'id' : 'password2',
            'required' : 'required',
        }
    ))
    
    class Meta:
        model = Usuario

        fields = ['username','nombre','apellido','email','fecha_nacimiento',]

        labels = {
            'username': 'Nombre de usuario',
            'nombre': 'Nombre',
            'apellido': 'Apellidos',
            'email': 'Correo',
            'fecha_nacimiento':'Fecha de nacimiento',
            }

        widgets = {
            'username': forms.TextInput(attrs={'class': 'mb-2 form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'mb-2 form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'mb-2 form-control'}),
            'email': forms.TextInput(attrs={'class': 'mb-2 form-control'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'mb-2 form-control'}),
            }
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Contraseñas no coinciden.')
        return password2

    def save(self, commit = True):
        user = super().save(commit = False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


    '''
    def __init__(self, *args, **kwargs):
        super(RegistroForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control'})
        '''
 