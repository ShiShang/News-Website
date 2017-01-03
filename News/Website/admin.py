from django.contrib import admin
from Website.models import News,Tags,Author,Users
#from django.db import models
# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    list_display=('Title','Create_Time','Modify_Time','Content')

class TagsAdmin(admin.ModelAdmin):
    list_display=('Group',)

class UserAdmin(admin.ModelAdmin):
    list_display=('Name','Birth','Profile')

class AuthorAdmin(admin.ModelAdmin):
    list_display=('Name','Profile')

admin.site.register(News,NewsAdmin)
admin.site.register(Tags,TagsAdmin)
admin.site.register(Users,UserAdmin)
admin.site.register(Author,AuthorAdmin)
