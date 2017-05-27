from django.forms.models import inlineformset_factory
from django.shortcuts import render_to_response, render, redirect
from django.utils import timezone
from .models import Produtos, Compra, ItensCompra
from .produto import ProdutosForm
from .compra import CompraForm, ItensCompraForms
from django.http import HttpResponseRedirect # Funcao para redirecionar o usuario
from django.contrib.auth.forms import UserCreationForm # Formulario de criacao de usuarios
from django.views.generic import View, TemplateView, CreateView

# pagina inicial
#class IndexView(TemplateView):
 #   def get(self, request):
  #      if request.user.is_authenticated:
   #         template_name = "estoque/index.html"
    #    return redirect('login')

    #index = IndexView.as_view()


def index(request):
    if request.user.is_authenticated:
        return render_to_response("estoque/index.html")
    return redirect('login')


#lista de produtos cadastrados
def produtos_list(request):
    produtos = Produtos.objects.filter(dtCriacao__lte=timezone.now()).order_by('dtCriacao')
    return render(request, 'estoque/produtos_list.html', {'produtos': produtos})

#Cria um novo produto
def produto_new(request):
    if request.method == "POST":
        form = ProdutosForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('produtos_list')
    else:
        form = ProdutosForm()
    return render(request, 'estoque/produto_edit.html', {'form': form})

#lista de compras
def compras_list(request):
    compras = Compra.objects.filter(dtCompra__lte=timezone.now()).order_by('dtCompra')
    return render(request, 'estoque/compras_list.html', {'compras': compras})

#Cria uma nova compra
def compras_new(request):
    if request.method == "POST":
        form = CompraForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('compras_list')
    else:
        form = CompraForm()
    return render(request, 'estoque/compras_edit.html', {'form': form})

def compra(request):
    compra_forms = Compra()
    item_compra_formset = inlineformset_factory(Compra, ItensCompra, form=ItensCompraForms, extra=0, can_delete=False, min_num=1, validate_min=True)

    if request.method == 'POST':
        forms = CompraForm(request.POST, request.FILES, instance=compra_forms, prefix='main')
        formset = item_compra_formset(request.POST, request.FILES, instance=compra_forms, prefix='product')

        if forms.is_valid() and formset.is_valid():
            forms = forms.save(commit=False)
            forms.save()
            formset.save()
            return HttpResponseRedirect('/pedido/')

    else:
        forms = CompraForm(instance=compra_forms, prefix='main')
        formset = item_compra_formset(instance=compra_forms, prefix='product')

    context = {
        'forms': forms,
        'formset': formset,
    }

    return render(request, 'estoque/itens_view.html', context)
'''
class itens_view(CreateView):
    template_name = "itens_view.html"
    form_class = CompraForm

    def get_context_data(self, **kwargs):
        context = super(itens_view, self).get_context_data(**kwargs)
        if self.request.POST:
            context['forms'] = CompraForm(self.request.POST)
            context['formset'] = ItemCompraFormSet(self.request.POST)
        else:
            context['forms'] = CompraForm()
            context['formset'] = ItemCompraFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        forms = context['forms']
        formset = context['formset']
        if forms.is_valid() and formset.is_valid():
            #self.object = form.save()
            forms.instance = self.object
            formset.instance = self.object
            forms.save()
            formset.save()
            return redirect('pedido')
        else:
            return self.render_to_response(self.get_context_data(form=form))
'''