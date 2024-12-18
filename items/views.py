from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, DetailView,
    CreateView, UpdateView,
    DeleteView
)
from .models import Item

class ItemListView(ListView):
    model = Item
    template_name = 'items/home.html'
    context_object_name = 'items'
    ordering = ['-date_posted']
    paginate_by = 8

class ItemDetailView(DetailView):
    model = Item

class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    fields = ['title', 'description', 'image', 'status', 'location']
    
    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)

class ItemUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Item
    fields = ['title', 'description', 'image', 'status', 'location']
    
    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        item = self.get_object()
        return self.request.user == item.posted_by

class ItemDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Item
    success_url = '/'
    
    def test_func(self):
        item = self.get_object()
        return self.request.user == item.posted_by