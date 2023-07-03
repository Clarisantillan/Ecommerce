from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import UserRegisterForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout, authenticate
from django.contrib import messages
#def autenticacion(request):
    
   #return render(request,'registro/registro.html')
   
class VRegistro(View):

   def get(self, request):
      form=UserCreationForm()
      return render(request, "registro/registro.html", {"form": form})
   
   def post(self,request):
      #rescato los datos del form
    form=UserCreationForm(request.POST)
    
    #si el fomulario es valido
    if form.is_valid():
      #guado la info del usuario en la base de datos
       usuario=form.save()
    
       login(request, usuario)
    
       return redirect('index')
    else:
       for msg in form.error_messages:
          messages.error(request, form.error_messages[msg])
          
         
       return render(request, "registro/registro.html", {"form": form})
    
def cerrar_session(request):
   logout(request)
   return redirect('index')

def loguear(request):
   if request.method == "POST":
      form=AuthenticationForm(request, data=request.POST)
      if form.is_valid():
         username=form.cleaned_data.get("username")
         password=form.cleaned_data.get("password")
         usuario=authenticate(username=username, password=password)
         if login(request, usuario) is not None:
            
            return redirect('index')
         else:
            messages.error(request,"usuario no valido")
      else:
         messages.error(request,"informacion incorrecta")      
   form= AuthenticationForm()
   return render(request, "login/login.html", {"form": form})