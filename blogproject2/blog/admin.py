from django.contrib import admin
from .models import Category,Tag,Post

admin.site.register(Post)


admin.site.register(Category)

admin.site.register(Tag)
# Register your models here.
