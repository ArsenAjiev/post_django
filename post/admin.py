from django.contrib import admin
from post.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "text", "created_at")
    fields = ("title", "text", "created_at")
    readonly_fields = ("created_at",)
    search_fields = ("title", "text")
