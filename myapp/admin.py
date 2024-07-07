from django.contrib import admin
from .models import Catagory,Post

# Register your models here.
@admin.register(Catagory)
class CatagoryAdmin(admin.ModelAdmin):
    list_display = ['title','image_tag','description','url','added_date']
    search_fields = ['title']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','image_tag','author','content','url','added_date','cat']
    search_fields = ['title']