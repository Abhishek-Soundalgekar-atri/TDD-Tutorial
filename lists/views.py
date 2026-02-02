from django.shortcuts import render, redirect

def home_page(request):
    # render template (we'll add items later)
    return render(request, "home.html")

def new_list(request):
    # temporary placeholder for POST handling (we'll implement saving later)
    if request.method == "POST":
        return redirect('home')
    return redirect('home')
