from django.shortcuts import render , redirect
from django.http import HttpResponse
from food.models import Item
from food.forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

# Create your views here.

# Function base index view

def index(request):
    itemlist = Item.objects.all()

    context = {
        'itemlist': itemlist,
    }
    return render(request , 'food/index.html' , context)


# Class base index view
class IndexClassView(ListView):

    model = Item
    context_object_name = 'itemlist'
    template_name = 'food/index.html'
    

# Function base detail view

def detail(request, item_id):
    item = Item.objects.get(pk=item_id)

    context = {

        'item' : item
    }
    return render(request, 'food/detail.html', context)

# Class base detail view

class FoodDetail(DetailView):

    model = Item
    context_object_name = 'item'
    template_name = 'food/detail.html'


# Function base create item view

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:index')

    context = {

        'form' : form
    }

    return render(request , 'food/item-form.html' , context)

# Class base create item view

class CreateItem(CreateView):

    model = Item
    fields = ['prod_code' , 'for_user' , 'Item_name' , 'Item_desc' , 'Item_price' , 'Item_image']
    template_name = 'food/item-form.html'
    success_url = reverse_lazy('food:index')

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# Function base update item view

def update_item(request , id):
    item = Item.objects.get(pk=id)
    form = ItemForm(request.POST or None , instance=item)

    context = {
        'form' : form
    }

    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request , 'food/item-form.html' , context)

# Function base delete item view

def delete_item(request , id):
    item = Item.objects.get(pk=id)

    context = {
        'item' : item
    }

    if request.method == 'POST':
        item.delete()
        return redirect('food:index')

    return render(request , 'food/item-delete.html',context)