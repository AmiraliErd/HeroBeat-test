from django.contrib import admin
from .models import Track, Album, Artist, Category, Comment

admin.site.register(Track)
admin.site.register(Category)
admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Comment)


# Register your models here.
