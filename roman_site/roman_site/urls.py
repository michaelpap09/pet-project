from django.contrib import admin
from django.urls import path, include
from django.urls import include, path, reverse_lazy
from django.views.generic import CreateView
from users.forms import CustomUserCreationForm

handler404 = 'core.views.error404'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include(('posts.urls', 'posts'), namespace='posts')),
    path('', include(('pages.urls', 'pages'), namespace='pages')),
    path('auth/', include('django.contrib.auth.urls')),
    path(
        'auth/registration/', 
        CreateView.as_view(
            template_name='registration/reg_form.html',
            form_class=CustomUserCreationForm,
            success_url=reverse_lazy('pages:index'),
        ),
        name='registration',
    ),
] 
