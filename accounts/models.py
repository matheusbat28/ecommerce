from django.db import models
from django.contrib.auth.models import AbstractUser
from cpf_field.models import CPFField

class User(AbstractUser):
    cpf = CPFField('cpf', blank=True, null=True)
    perfil_img = models.ImageField(upload_to='perfil_img', blank=True, null=True)
    telephone = models.CharField(max_length=50, blank=True, null=True)   
    class Meta:
        db_table = 'user'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        
    def __str__(self):
        return self.username