from django.contrib import admin
from users.models import NewUser
from .models import Tag, Comment, Post

class IceCreamAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'desc',
        'year',
        'pub_date',
    )
    list_editable = (
        'title',
        'desc',
        'year'
    )    

admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(NewUser)
