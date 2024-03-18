from django.shortcuts import render

def barra(request):
    return render(request,"barra.html",{})

