from django.shortcuts import render
from perfis.models import Perfil
# Create your views here.
def index(request):
    return render(request,'index.html',{'perfis': Perfil.objects.all(), 'perfil_logado' : get_perfil_logado(request)})

def exibir(request, perfil_id):

    perfil = Perfil.objects.get(id=perfil_id)

    return render(request, 'perfil.html', {'perfil': perfil,'perfil_logado': get_perfil_logado(request)})    

def convidar(request, perfil_id):
    perfil_a_convidar = Perfil.objects.get(id=perfil_id)
    perfil_logado = get_perfil_logado(request)
    pperfil_logado.convidar(perfil_a_convidar)

def get_perfil_logado(request):   
    return Perfil.objects.get(id=3)
    
      

      