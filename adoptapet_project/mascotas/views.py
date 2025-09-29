# mascotas/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Mascota, SolicitudAdopcion

def home(request):
    perros = Mascota.objects.filter(tipo='Perro', disponible=True)
    gatos = Mascota.objects.filter(tipo='Gato', disponible=True)
    return render(request, 'mascotas/home.html', {'perros': perros, 'gatos': gatos})

def contacto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        mensaje = request.POST.get('mensaje')

        # Aquí puedes enviar un correo (opcional)
        # send_mail(
        #     f'Mensaje de {nombre}',
        #     mensaje,
        #     settings.DEFAULT_FROM_EMAIL,
        #     [settings.DEFAULT_FROM_EMAIL],
        # )

        messages.success(request, '¡Gracias! Tu mensaje ha sido enviado.')
        return redirect('contacto')

    return render(request, 'mascotas/contacto.html')

def nosotros(request):
    return render(request, 'mascotas/nosotros.html')

def adopcion(request):
    perros = Mascota.objects.filter(tipo='Perro')
    gatos = Mascota.objects.filter(tipo='Gato')
    return render(request, 'mascotas/adopcion.html', {'perros': perros, 'gatos': gatos})

def adoptar_modal(request):
    if request.method == 'POST':
        mascota_id = request.POST.get('mascota_id')
        mascota = get_object_or_404(Mascota, id=mascota_id)

        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        rut = request.POST.get('rut')
        correo = request.POST.get('correo')
        telefono = request.POST.get('telefono', '')
        motivo = request.POST.get('motivo')

        # Crear la solicitud
        SolicitudAdopcion.objects.create(
            mascota=mascota,
            nombre=nombre,
            apellido=apellido,
            rut=rut,
            correo=correo,
            telefono=telefono,
            motivo=motivo
        )

        messages.success(request, f"¡Solicitud enviada para adoptar a {mascota.nombre}!")
        return redirect('adopcion')  
    
    return redirect('adopcion')
