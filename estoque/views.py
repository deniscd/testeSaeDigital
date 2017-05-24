from django.shortcuts import render
from django.shortcuts import redirect
from django.utils import timezone
from .models import Produtos
from .produto import ProdutosForm

def produtos_list(request):
    produtos = Produtos.objects.filter(dtCriacao__lte=timezone.now()).order_by('dtCriacao')
    return render(request, 'estoque/produtos_list.html', {'produtos': produtos})

def produto_new(request):
    if request.method == "POST":
        form = ProdutosForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.idProduto = request.user
            post.save()
            return redirect('produtos_list')
    else:
        form = ProdutosForm()
    return render(request, 'estoque/produto_edit.html', {'form': form})