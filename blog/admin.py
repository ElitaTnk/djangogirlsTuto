from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'status')
    actions = ['make_published']

    def make_published(self, request, queryset):
        rows_updated = queryset.update(status='p')
        if rows_updated == 1:
            message_bit = "1 post was"
        else:
            message_bit = "%s posts were" % rows_updated
        self.message_user(request, "%s successfully marked as published." % message_bit)

admin.site.register(Post, PostAdmin)
