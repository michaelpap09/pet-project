from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include(('posts.urls', 'posts'), namespace='posts')),
    path('', include(('pages.urls', 'pages'), namespace='pages')),
    path('auth/', include('django.contrib.auth.urls')),
]
