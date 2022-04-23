from django.shortcuts import render
from django.http import HttpResponse

class Dog:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

dogs = [
  Dog('Princess', 'chihuahua', '12 lb devil', 15),
  Dog('Captain', 'terrier mix', 'kind and chunky white terrier', 10),
  Dog('Keanu', 'cardigan corgi', 'energetic black puppy', 0),
]

# Create your views here.
def home(req):
  return HttpResponse('Home page!')

def about(req):
  return render(req, 'about.html')

def dogs_index(req):
  return render(req, 'dogs/index.html', {'dogs': dogs})