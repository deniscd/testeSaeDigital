from django.shortcuts import render

def produtos_list(request):
    return render(request, 'estoque/produtos_list.html', {})