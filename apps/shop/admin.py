from django.contrib import admin
from .models import Category, Product
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 10


admin.site.register(Category,CategoryAdmin)



class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','slug','price','stock','available','created','updated']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['stock','price','available']
    list_per_page = 10
    # list_filter = ['name','price','stock','available']
    

admin.site.register(Product,ProductAdmin)
