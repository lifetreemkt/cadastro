from django.shortcuts import render
from .models import Produto

def home(request):
    return render(request, 'produtos/home.html')
def produtos(request):
    novo_produto = Produto()
    novo_produto.nome = request.POST.get('nome')
    novo_produto.descricao = request.POST.get('descricao')
    novo_produto.preco = request.POST.get('preco')
    novo_produto.validade = request.POST.get('validade')

    novo_produto.save() #necessario salvar no banco de dados

    produtos = dict(
        produtos = Produto.objects.all())
    return render(request, 'produtos/produtos.html', produtos)