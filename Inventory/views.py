from django.views import View
from django.views.generic import FormView, CreateView, UpdateView, ListView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .models import Item
from .forms import AddItem, FindItem

decorators = [login_required]

@method_decorator(decorators, name='dispatch')
class HomeView(ListView):
    model = Item
    template_name = 'home.html'
    context_object_name = 'items'

@method_decorator(decorators, name='dispatch')
class AddItemView(CreateView):
    model = Item
    form_class = AddItem
    template_name = 'add_items.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request, 'Record added successfully!')
        return super().form_valid(form)

@method_decorator(decorators, name='dispatch')
class FindItemView(FormView):
    template_name = 'find_items.html'
    form_class = FindItem

    def get(self, reqest, *args, **kwargs):
        form = self.get_form()
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

        return self.render_to_response(self.get_context_data(form=form, items=items))
    
    def form_invalid(self, form):
        items = Item.objects.all()
        return self.render_to_response(self.get_context_data(form=form, items=items))

class CustomLoginView(LoginView):
    template_name = 'login.html'

    def form_valid(self, form):
        messages.success(self.request, 'You have been logged in!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.success(self.request, 'There was an error. Please try again.')
        return super().form_invalid(form)
    
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        messages.success(self.request, 'You have been logged out.')
        return super().dispatch(request, *args, **kwargs)
    
@method_decorator(decorators, name='dispatch')
class DeleteItemView(View):
    def post(self, request, pk):
        item = Item.objects.get(pk=pk)
        item.delete()
        messages.success(request, 'Item deleted successfully.')
        return redirect('home')
    
@method_decorator(decorators, name='dispatch')
class EditItemView(UpdateView):
    model = Item
    form_class = AddItem
    template_name = 'edit_item.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request, 'Item edited successfully.')
        return super().form_valid(form)
'''
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
'''