# myapp/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Products
from .forms import ProductsForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template.loader import render_to_string

@login_required
def index(request):
    query = request.GET.get('q')
    products = Products.objects.all()

    if query:
        artikuls = [artikul.strip() for artikul in query.split(' ')]
        products = products.filter(артикул__in=artikuls)

    paginator = Paginator(products, 100)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'index.html', {'page_obj': page_obj, 'query': query})

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductsForm()
    return render(request, 'add_product.html', {'form': form})

@login_required
def edit_product(request, pk):
    product = get_object_or_404(Products, pk=pk)
    if request.method == 'POST':
        form = ProductsForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductsForm(instance=product)
    return render(request, 'edit_product.html', {'form': form, 'product': product})

def live_search(request):
    query = request.GET.get('q', '')
    results = Products.objects.filter(
        Q(артикул__icontains=query) |
        Q(наименование_ru__icontains=query) |
        Q(наименование_en__icontains=query) |
        Q(наименование_de__icontains=query)
    )[:100]  # Limit the number of results displayed

    html = render_to_string('live_search_results.html', {'results': results})
    return HttpResponse(html)
