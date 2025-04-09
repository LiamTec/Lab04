# agenda/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Contacto
from .forms import ContactoForm

# Vista para listar los contactos
def lista_contactos(request):
    contactos = Contacto.objects.all()
    return render(request, 'agenda/lista_contactos.html', {'contactos': contactos})

# Vista para agregar un contacto
def agregar_contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_contactos')
    else:
        form = ContactoForm()
    return render(request, 'agenda/agregar_contacto.html', {'form': form})

# Vista para editar un contacto
def editar_contacto(request, pk):
    contacto = get_object_or_404(Contacto, pk=pk)
    if request.method == 'POST':
        form = ContactoForm(request.POST, instance=contacto)
        if form.is_valid():
            form.save()
            return redirect('lista_contactos')
    else:
        form = ContactoForm(instance=contacto)
    return render(request, 'agenda/editar_contacto.html', {'form': form})

# Vista para eliminar un contacto
def eliminar_contacto(request, pk):
    contacto = get_object_or_404(Contacto, pk=pk)
    if request.method == 'POST':
        contacto.delete()
        return redirect('lista_contactos')
    return render(request, 'agenda/eliminar_contacto.html', {'contacto': contacto})
