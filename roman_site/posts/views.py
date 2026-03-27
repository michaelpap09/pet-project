from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from .models import Post, Tag
from .forms import Form, TextForm


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

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form) 


class Erase(UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('posts:list')
    context_object_name = 'post'
    template_name = "form.html"
    
    def test_func(self):
        object = self.get_object()
        return object.author == self.request.user 


class EditPost(UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'desc', 'year']
    context_object_name = 'post'
    template_name = "form.html"
    success_url = reverse_lazy('posts:list')

    def test_func(self):
        object = self.get_object()
        return object.author == self.request.user 


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TextForm()
        context['congratulations'] = (
            self.object.congratulations.select_related('author')
        )
        context['tag'] = Tag.objects.all()
        return context


@login_required
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = TextForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.post = post
        comment.save()
    return redirect('posts:post', pk=pk)