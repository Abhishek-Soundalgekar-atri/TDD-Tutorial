from django.shortcuts import render, redirect
from .models import Item

def home_page(request):
    all_items = Item.objects.all()
    return render(request, "home.html", {'items': all_items})


def new_list(request):
    if request.method == "POST":
        Item.objects.create(text=request.POST.get('item_text', ''))
        return redirect('home')
    return redirect('home')
