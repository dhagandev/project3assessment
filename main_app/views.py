from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView
from .models import Item

# Create your views here.
class ItemList(ListView):
	model = Item

class AddItem(CreateView):
	model = Item
	fields = '__all__'

class DeleteItem(DeleteView):
	model = Item
	success_url = '/'