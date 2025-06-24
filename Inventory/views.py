from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Item
from .forms import AddItem, FindItem

@login_required
def home(request):
    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})

@login_required
def add_items(request):
    form = AddItem(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Record added successfully!')
            return redirect('home')
    else:
        return render(request, 'add_items.html', {'form': form})

@login_required
def find_items(request):
    form = FindItem(request.GET or None)
    items = Item.objects.all()
    if form.is_valid():
        name = form.cleaned_data.get('name')
        spot = form.cleaned_data.get('spot')
        location = form.cleaned_data.get('location')
        start_date = form.cleaned_data.get('start_date')
        end_date = form.cleaned_data.get('end_date')
        if name:    
            items = items.filter(name__icontains=name)
        if spot:
            items = items.filter(spot__icontains=spot)
        if location:
            items = items.filter(location=location)
        if start_date:
            items = items.filter(date__gte=start_date)
        if end_date:
            items = items.filter(date__lte=end_date)
            
    return render(request, 'find_items.html', {'form': form, 'items': items})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You have been logged in."))
            return redirect('home')
        else:
            messages.success(request, ("There was an error. Please try again."))
            return redirect('login')
    else:
        return render(request, 'login.html', {})

@login_required
def logout_user(request):
    logout(request)
    messages.success(request, ("You have been logged out."))
    return redirect('home')

@login_required
def delete_item(request, pk):
    delete_it = Item.objects.get(id=pk)
    delete_it.delete()
    messages.success(request, ("Item deleted successfully."))
    return redirect('home')

@login_required
def edit_item(request, pk):
    item = Item.objects.get(id=pk)
    form = AddItem(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        messages.success(request, ("Item edited successfully."))
        return redirect('home')
    else:
        return render(request, 'edit_item.html', {'form': form})