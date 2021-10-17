#siempre son estas librerías
#trabajar con modelos en general
from django.db import models
#cuestiones genéricas de gestión de usuarios
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
#la funcion make_password que va a recibir el password original y genera una contraseña ecriptada
from django.contrib.auth.hashers import make_password

class UserManager (BaseUserManager):
    def create_user(self,username, password = None ):
        #si el usuario viene vacio entonces , haga lo siguiente
        if not username:
            raise ValueError('El usuario debe tener o llegar con un username')
        #en el caso de que si llegue el username, ahora se utiliza el BaseUserManager para administrar usuarios
        #se crea un modelo del usuario base,donde el username que recibe es igual al username que está llegando como parámetro
        user = self.model(username = username)
        #a ese username se le hará ahora la configuración del password, es decir al usuario anterior agregarle el siguiente password
        user.set_password(password)
        #ahora ya creado el usuario, con el username, con el password y ahora a guardarlo, con el using se utiliza para guardar
        #en una base de datos en los settings 
        #esta funcion save funciona igual que el comando de insertar en una bas de datos
        user.save(using = self._db)
        #retornamos la información del usuario
        return user

    #crear usuarios administradores
    def create_superuser(self, username_, password_):
        #asignar a username y password lo que recibe para ambos
        user = self.create_user(username = username_, password = password_)
        #si se quiere que sea administrador es igual a True
        user.is_admin = True
        user.save(using = self._db)
        return user 

#crear el model
class User(AbstractBaseUser,PermissionsMixin):
    #atributo , id del usuario
    id = models.BigAutoField(primary_key=True)
    username = models.CharField('Username',max_length=45,unique=True)
    password = models.CharField('Password',max_length=256)
    name = models.CharField('nombre',max_length=50)
    email = models.EmailField('Email',max_length=100)

    def save(self,**kwargs):
        some_salt = 'MkgasdDEeadfadsGasdfASDFAEdasdgFFF'
        self.password = make_password(self.password,some_salt)
        super().save(**kwargs)
    
    objects = UserManager()
    USERNAME_FIELD = 'username'