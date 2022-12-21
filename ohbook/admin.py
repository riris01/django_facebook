from django.contrib import admin

from ohbook.models import Article

admin.site.register(Article)

from ohbook.models import Comment

admin.site.register(Comment)
# Register your models here.
