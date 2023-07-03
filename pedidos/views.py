from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from carro.carro import Carro
from pedidos.models import Pedido, LineaPedido
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
@login_required(login_url="/autenticacion/loguear")


def procesar_pedido(request):
    pedido=Pedido.objects.create(user=request.user)#saber quien hizo el inicio de sesion
    carro= Carro(request)
    lineas_pedido=list()
    for key,value in carro.carro.items():#recorro el carro y rescto los datos
        lineas_pedido.append(LineaPedido(
            
            producto_id=key,
            cantidad=value['cantidad'],
            user=request.user,
            pedido=pedido
        ))
    
    LineaPedido.objects.bulk_create(lineas_pedido)#aca metemos todo en la base de datos
    enviar_mail(
        pedido=pedido,
        lineas_pedido=lineas_pedido,
        nombreusuario=request.user.username, 
        email_usuario=request.user.email
    )
    messages.success(request, "El pedido se ha enviado correctamente")
    
    return redirect("../tienda")

def enviar_mail(**kwargs):
    asunto= "Nuevo pedido en Casa Limpia"
    mensaje= render_to_string("emails/pedido.html", {
        "pedido": kwargs.get("pedido"),
        "lineas_pedido":kwargs.get("lineas_pedido"),
        "nombreusuario": kwargs.get("nombreusuario"),
    })
    mensaje_texto=strip_tags(mensaje)
    from_email="clara.santillan.01@gmail.com"
    to="atelajuan12@gmail.com"
    
    send_mail(asunto, mensaje_texto, from_email,[to], html_message=mensaje)