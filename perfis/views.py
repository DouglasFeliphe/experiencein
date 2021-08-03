from django.shortcuts import redirect, render
from perfis.models import Convite, Perfil
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.

@login_required
def index(request):
    print(request.user.username) #novo
    print(request.user.email) #novo
    print(request.user.has_perm('perfis.redirect')) #novo

    return render(
        request,'index.html',
        {
        'perfis': Perfil.objects.exclude(nome=request.user.perfil.nome), 
        'perfil_logado' : get_perfil_logado(request)
        })

@login_required
def exibir(request, perfil_id):
    perfil = Perfil.objects.get(id=perfil_id)
    perfil_logado = get_perfil_logado(request)
    ja_e_contato = perfil in perfil_logado.contatos.all()
    return render(request,'perfil.html',{'perfil':perfil,'perfil_logado':perfil_logado,'ja_e_contato':ja_e_contato})

@permission_required('perfis.add_convite',raise_exception=True)
@login_required
def convidar(request, perfil_id):
    perfil_a_convidar = Perfil.objects.get(id=perfil_id)
    perfil_logado = get_perfil_logado(request)
    perfil_logado.convidar(perfil_a_convidar)
    return redirect('index')

@login_required
def get_perfil_logado(request):   
    return request.user.perfil

@login_required
def aceitar(request,convite_id):
    convite = Convite.objects.get(id=convite_id) 
    convite.aceitar()  
    return redirect('index')


      

      