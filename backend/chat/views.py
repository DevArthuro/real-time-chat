from django.shortcuts import render
from django.views import View

def index(request):
    context = {
        "title": "dashboard",
        "counter": 100,
        "data": (0,0,0,0,0,0,0)
    }
    return render(request, 'chat/dashboard.html', context)

class DetailView(View):
    def get(self, request, slug):
        context = {
            "title": slug
        }
        return render(request, "chat/detail-chat.html", context)