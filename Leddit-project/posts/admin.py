from django.contrib import admin
from .models import Post, Vote



class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url', 'poster', 'created_at')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'poster')


class VoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'voter', 'post')
    list_display_links = ('id',)
    search_fields = ('voter', 'post')


admin.site.register(Post, PostAdmin)
admin.site.register(Vote, VoteAdmin)


