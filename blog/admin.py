from django.contrib import admin
from .models import Post
# Register your models here.

class PostAdminModel(admin.ModelAdmin):
    list_display = ["title", "publish_date", "update_date"]
    list_filter = ["publish_date"]
    search_fields = ["title", "content"]

    class Meta:
        model = Post

admin.site.register(Post, PostAdminModel)
