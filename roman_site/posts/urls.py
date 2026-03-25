from django.urls import path
from django.views.generic import TemplateView, CreateView, ListView

from . import views

app_name = 'posts'

urlpatterns = [
    path(
        '',
        views.List.as_view(template_name="posts/list.html",),
        name='list'
    ),
    path(
        '<int:pk>/',
        views.Post.as_view(template_name="posts/post.html",),
        name='post'
    ),
    path(
        '<int:pk>/edit/',
        views.EditPost.as_view(template_name="posts/form.html",),
        name='edit'
    ),
    path(
        '<int:pk>/delete/',
        views.Erase.as_view(template_name="posts/form.html",),
        name='delete'
    ),
    path(
        'form/',
        views.Create.as_view(template_name="posts/form.html",),
        name='form'
    ),
]
