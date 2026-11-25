from django.shortcuts import render


def index(request):
    return render(request, "web/index.html")


def login_view(request):
    return render(request, "web/login.html")


def panel(request):
    contexto = {
        "usuarios": 1248,
        "ventas": 84300,
    }
    return render(request, "web/panel.html", contexto)