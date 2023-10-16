from django.shortcuts import render

def index(request):
    context = {
        "name": "carlos"
    }
    return render(request, 'index.html', context)