from django.contrib import admin
from .models import *

# Register your models here.

# admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Company)
admin.site.register(ProductSite)
admin.site.register(ProductSize)
admin.site.register(Comment)

admin.site.site_header = "Product Review Admin"


@admin.register(Product)
class ProductAmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'content',)
    # list_filter = ('category',)
