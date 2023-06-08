from django.shortcuts import render
# example/views.py
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Person

class PersonList(ListView):
    model = Person
    template_name = 'person_list.html'

class PersonCreate(CreateView):
    model = Person
    fields = ['name', 'age']
    template_name = 'person_create.html'
    success_url = reverse_lazy('person_list')

class PersonUpdate(UpdateView):
    model = Person
    fields = ['name', 'age']
    template_name = 'person_update.html'
    success_url = reverse_lazy('person_list')

class PersonDelete(DeleteView):
    model = Person
    template_name = 'person_delete.html'
    success_url = reverse_lazy('person_list')

