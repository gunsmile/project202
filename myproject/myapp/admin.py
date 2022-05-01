from django.contrib import admin

# Register your models here.
from myapp.models import Profile, Item, OrderItem

class ProfileAdmin(admin.ModelAdmin):
    pass
admin.site.register(Profile, ProfileAdmin)

class ItemAdmin(admin.ModelAdmin):
    list_display=['title','unit_price','description']
    pass
admin.site.register(Item, ItemAdmin)

class OrderItemAdmin(admin.ModelAdmin):
    list_display_links = ('profile',)
    list_display = ('profile','item','quantity')
    list_editable = ('item','quantity')
admin.site.register(OrderItem, OrderItemAdmin)

# class SaleOrderAdmin(admin.ModelAdmin):
#     pass
# admin.site.register(SaleOrder, SaleOrderAdmin)