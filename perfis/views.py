from django.shortcuts import render
from perfis.models import Perfil
# Create your views here.
def index(request):
    return render(request,'index.html')

def exibir(request, perfil_id):

    perfil = Perfil()

    if (perfil_id == 1):
        perfil = Perfil("Fulano",'@teste.com','333333','IFB')

    if (perfil_id == 2):
        perfil = Perfil("Siclano",'@dama.com','777777','UNG')
   
    return render(request, 'perfil.html', {'perfil': perfil})    