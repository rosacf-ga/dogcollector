from django.shortcuts import render
from django.http import HttpResponse
from .models import Dog
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class DogCreate(CreateView):
  model = Dog 
  fields = '__all__'

class DogUpdate(UpdateView):
  model = Dog 
  fields = ['breed', 'description', 'age']

class DogDelete(DeleteView):
  model = Dog 
  success_url = '/dogs/'

# Create your views here.
def home(req):
  return HttpResponse('Home page!')

def about(req):
  return render(req, 'about.html')

def dogs_index(req):
  dogs = Dog.objects.all()
  return render(req, 'dogs/index.html', {'dogs': dogs})

def dogs_detail(req, dog_id):
  dog = Dog.objects.get(id=dog_id)
  return render(req, 'dogs/detail.html', {'dog': dog})