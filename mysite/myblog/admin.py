from django.contrib import admin
from myblog.models import Post
from myblog.models import Category

# Register your models here.
admin.site.register(Post)
admin.site.register(Category)


class CategoryAdmin(admin.ModelAdmin):
    fields = ('name', 'description')


class CategoryAdmin(admin.ModelAdmin):
    exclude = ('Post',)
