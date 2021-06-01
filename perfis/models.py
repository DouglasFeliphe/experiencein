from django.db import models

# Create your models here.
class Perfil(object):
    def __init__(self, nome='',email='', telefone='', nome_da_empresa=''):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.nome_da_empresa = nome_da_empresa
