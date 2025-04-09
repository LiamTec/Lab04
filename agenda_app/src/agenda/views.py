from django.shortcuts import render, get_object_or_404, redirect
from .models import Contacto
from .forms import ContactoForm

# Ver lista de contactos
def lista_contactos(request):
    contactos = Contacto.objects.all()
    return render(request, 'agenda/lista.html', {'contactos': contactos})

# Agregar contacto
def agregar_contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_contactos')
    else:
        form = ContactoForm()
    return render(request, 'agenda/agregar.html', {'form': form})

# Editar contacto
def editar_contacto(request, pk):
    contacto = get_object_or_404(Contacto, pk=pk)
    if request.method == 'POST':
        form = ContactoForm(request.POST, instance=contacto)
        if form.is_valid():
            form.save()
            return redirect('lista_contactos')
    else:
        form = ContactoForm(instance=contacto)
    return render(request, 'agenda/editar.html', {'form': form})

# Eliminar contacto
def eliminar_contacto(request, pk):
    contacto = get_object_or_404(Contacto, pk=pk)
    if request.method == 'POST':
        contacto.delete()
        return redirect('lista_contactos')
    return render(request, 'agenda/eliminar.html', {'contacto': contacto})
