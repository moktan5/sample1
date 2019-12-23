from django.db import models
from django.contrib.auth.models import  AbstractUser
from django.utils.translation import  gettext_lazy as _
from django.conf import  settings

# Create your models here.

class User(AbstractUser):
    Roles = (("0","Department"),("1","Teacher"),("2","Student"))
    role = models.CharField(max_length=1,choices=Roles)
    is_department=models.BooleanField(default=False)
    is_Teacher= models.BooleanField(default=False)
    is_Student = models.BooleanField(default=True)
    email= models.EmailField(_('email address'),blank=False,unique=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = 'role','email'
