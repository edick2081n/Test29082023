from django.shortcuts import render
from prodaga.models import Flat


def show_flats(request):
    flat_list = Flat.objects.all()
    if 'sort' in request.GET:
        flat_list = flat_list.order_by("square")
    return render(request, 'prodaga/flat.html', {'flat_list': flat_list})

def detail_flat(request, flat_id):
    flat = Flat.objects.get(id=flat_id)
    return render(request, 'prodaga/detail.html', {"flat": flat})
