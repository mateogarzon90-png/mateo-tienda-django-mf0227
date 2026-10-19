from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm
from .dominio import ProductoBase, ProductoOferta  

def lista_productos(request):
    productos_db = Producto.objects.all()
    productos_mostrar = []

    for p in productos_db:
        
        if p.descuento > 0:
            prod_obj = ProductoOferta(p.nombre, float(p.precio), p.descuento)
        else:
            prod_obj = ProductoBase(p.nombre, float(p.precio))
        
        productos_mostrar.append({
            'nombre': p.nombre,
            'precio_original': p.precio,
            'descuento': p.descuento,
            'precio_final': prod_obj.precio_final()
        })

    return render(request, 'catalogo/lista.html', {'productos': productos_mostrar})

def nuevo_producto(request):
    # Guardar los registros mediante POST y redirigir al listado
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    
    return render(request, 'catalogo/nuevo.html', {'form': form})