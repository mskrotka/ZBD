from django.contrib import admin
from .models import Wplyw


# admin.site.register(Wplyw)

@admin.register(Wplyw)
class WplywAdmin(admin.ModelAdmin):
    # fields = ('name', 'category', 'inflow')
    list_display = ('name', 'kategoria1', 'flow', 'how_much', 'category')
    list_filter = ('name', 'how_much', 'category')
    search_fields = ('name', 'how_much')



