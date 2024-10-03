from django.shortcuts import render

# Create your views here.

def home(request):
    
    context = {
        'title': 'Home',
        'text': 'Olá home!'
    }
    
    return render(
        request,
        'home/index.html',
        context
    )
