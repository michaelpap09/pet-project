from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Post
from .forms import Form


class List(LoginRequiredMixin, ListView):
    model = Post
    template_name = "list.html"
    context_object_name = 'posts'
    login_url = 'login'


class Create(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "form.html"
    success_url = reverse_lazy('pages:index')
    form_class = Form
    context_object_name = 'form'
    login_url = 'login'


class Erase(DeleteView):
    model = Post
    success_url = reverse_lazy('posts:list')
    context_object_name = 'post'
    template_name = "form.html"


class EditPost(UpdateView):
    model = Post
    fields = ['title', 'desc', 'year']
    context_object_name = 'post'
    template_name = "form.html"


class Post(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
