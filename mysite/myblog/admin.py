from django.contrib import admin
from myblog.models import Post
from myblog.models import Category

# Register your models here.
#admin.site.register(Post)
#admin.site.register(Category)

class CategoryInline(admin.TabularInline):
    model = Category.post.through

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [
        CategoryInline,
    ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    exclude = ('Post',)
