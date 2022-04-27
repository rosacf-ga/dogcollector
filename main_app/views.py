from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Dog
from .forms import FeedingForm
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
  feeding_form = FeedingForm()
  return render(req, 'dogs/detail.html', {'dog': dog, 'feeding_form': feeding_form})

def add_feeding(request, dog_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.dog_id = dog_id 
    new_feeding.save()
  return redirect('detail', dog_id=dog_id)
