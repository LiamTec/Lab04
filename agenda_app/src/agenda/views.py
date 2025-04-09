from django.shortcuts import render, redirect, get_object_or_404
from .models import Contacto
from .forms import ContactoForm

def lista_contactos(request):
    contactos = Contacto.objects.all()
    return render(request, 'contactos/lista.html', {'contactos': contactos})

def agregar_contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_contactos')
    else:
        form = ContactoForm()
    return render(request, 'contactos/formulario.html', {'form': form})

def editar_contacto(request, pk):
    contacto = get_object_or_404(Contacto, pk=pk)
    if request.method == 'POST':
        form = ContactoForm(request.POST, instance=contacto)
        if form.is_valid():
            form.save()
            return redirect('lista_contactos')
    else:
        form = ContactoForm(instance=contacto)
    return render(request, 'contactos/formulario.html', {'form': form})

def eliminar_contacto(request, pk):
    contacto = get_object_or_404(Contacto, pk=pk)
    if request.method == 'POST':
        contacto.delete()
        return redirect('lista_contactos')
    return render(request, 'contactos/eliminar.html', {'contacto': contacto})
