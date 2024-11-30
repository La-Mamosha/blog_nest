from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm

##########################################################################################################################
class RegistrationForm(UserCreationForm):
    class Meta: # Data en la cual crearemos el formulario
        model = User
        fields = ('email', 'username', 'password1', 'password2') #Campos que queremos que nos mande el formulario
        
    def save(self, comit=True):
        user = super(RegistrationForm, self).save(commit=False) #self = Intancia de si mismo (RegistrationForm)
        user.email = self.cleaned_data['email'] #Guardamos el email
        user.is_staff = True #Iniciar sesion en el portal. Darle permiso de admin
        
        if comit:
            user.save() #Guardamos el usuario en la base de datos
        return user #Retornamos el usuario
            

##########################################################################################################################
