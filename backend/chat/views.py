from django.shortcuts import render

def index(request):
    context = {
        "title": "dashboard",
        "counter": 100,
        "data": (5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5)
    }
    return render(request, 'chat/dashboard.html', context)