from django.contrib import admin
from .models import Picture, Filter, User, Order
# Admin UI
class PieceDisplay(admin.ModelAdmin):
    list_display = []
    list_display = ('name', 'price', 'sort')
    ordering = ('price',)
    search_fields = ('name',)


# Register your models here.
admin.site.register(Picture, PieceDisplay)
admin.site.register(Filter)
admin.site.register(User)
admin.site.register(Order)