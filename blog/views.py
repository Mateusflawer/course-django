from django.shortcuts import render

# Create your views here.

def blog(request):
    context = {
        'title': 'Blog',
        'text': 'Olá blog!',
    }
    
    return render(
        request,
        'blog/index.html',
        context,
    ) 


def exemplo(request):
    context = {
        'title': 'Exemplo',
        'text': 'Olá exemplo!',
    }
    
    return render(
        request,
        'blog/exemplo.html',
        context
    )
