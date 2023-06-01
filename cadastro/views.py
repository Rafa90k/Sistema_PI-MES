from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import cadastro_of
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages import constants

# Create your views here.
@login_required
def cadastrar_of(request):
    if request.method == "GET":
        of = request.GET.get('filtro_of')        
        cadastros = cadastro_of.objects.all()
        if of:
            cadastros = cadastros.filter(numero_da_of=of)
        return render(request, 'cadastro/cadastrar_of.html', {'cadastros': cadastros})        
    elif request.method == "POST":
        numero_da_of = request.POST.get('numero_da_of')
        codigo_produto = request.POST.get('codigo_produto')
        produto = request.POST.get('produto')
        quantidade_of = request.POST.get('quantidade_of')

        cadastro = cadastro_of(
            criador = request.user,
            numero_da_of = numero_da_of,
            codigo_produto = codigo_produto,
            produto = produto,
            quantidade_of = quantidade_of,
        )

        cadastro.save()

        messages.add_message(request, constants.SUCCESS, 'O.F cadastrada com sucesso.')
        return redirect(reverse('cadastrar_of'))


@login_required
def editar_of(request, id):
    of = cadastro_of.objects.get(id=id)
    return render(request, "cadastro/editar_of.html", {"of": of})


@login_required
def update(request, id):
    numero_da_of = request.POST.get("numero_da_of")
    codigo_produto = request.POST.get("codigo_produto") 
    produto = request.POST.get("produto") 
    quantidade_of = request.POST.get("quantidade_of") 
    of = cadastro_of.objects.get(id=id)                
    of.numero_da_of = numero_da_of
    of.codigo_produto = codigo_produto
    of.produto = produto
    of.quantidade_of = quantidade_of     
    of.save()
    return redirect(reverse('ofs_cadastradas'))


@login_required
def delete(request, id):
    of = cadastro_of.objects.get(id=id)
    of.delete()
    return redirect(reverse('ofs_cadastradas'))
       

@login_required
def deletar_of(request):
    pass


@login_required
def ofs_cadastradas(request):
    if request.method == "GET":
        of = request.GET.get('filtro_of')        
        cadastros = cadastro_of.objects.all()
        if of:
            cadastros = cadastros.filter(numero_da_of=of)
        return render(request, 'cadastro/ofs_cadastradas.html', {'cadastros': cadastros})        
    




    



