from django.shortcuts import render,redirect
from django.contrib import messages
from miformulario.models import Usuario
# Create your views here.




def index(request):
     return render(request,'index.html')


def registro(request):
     registro = "Formulario de Registro"
     
     return render(request,'registro.html',{
         'registro':registro
     })


def exito_registro(request):
    if request.method == 'POST':

        nombre = request.POST['nombre']
        email = request.POST['email']
        password = request.POST['password']
        direccion = request.POST['direccion']

        usuario = Usuario(
            nombre = nombre,
            email = email,
            password = password,
            direccion = direccion
        )
        usuario.save()
        messages.success(request,f"Bienvenido {usuario.nombre}")
        return redirect('inicio')
    else:
        return HttpResponse("<h2>No se ha podido crear al usuario</h2>")
