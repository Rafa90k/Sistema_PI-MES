from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from cadastro.models import cadastro_of



# Create your views here.
@login_required
def monitoramento(request):
    if request.method == "GET":
        return render(request, 'monitoramento/monitoramento.html')


def logout(request):
    user = auth.logout(request)
    return redirect('login/')


@login_required
def maquina(request):
    if request.method == "GET":
        return render(request, 'monitoramento/maquina.html')
    
    if request.method == "POST":
        of = request.POST.get('of6numeros')
        cadastros = cadastro_of.objects.all()
        if of:
            cadastros = cadastros.filter(numero_da_of=of)
        return render(request, 'monitoramento/maquina.html', {'cadastros': cadastros})
    
   
