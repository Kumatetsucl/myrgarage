from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request,'index.html')

def alinyBalan(request):
    return render(request,'alinyBalan.html')

def frenos(request):
    return render(request,'frenos.html')

def diagnostico(request):
    return render(request,'diagnostico.html')

def contacto(request):
    return render(request,'contacto.html')

def loggin(request):
    return render(request,'loggin.html')