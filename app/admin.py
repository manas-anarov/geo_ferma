from django.contrib import admin
from .models import Farmer, Culture, Season, Plot

admin.site.register(Farmer)
admin.site.register(Culture)
admin.site.register(Season)


@admin.register(Plot)
class PlotAdmin(admin.ModelAdmin):
    list_display = ('id', 'farmer', 'culture', 'season', 'contour')
    list_filter = ('farmer', 'culture')
    search_fields = ('farmer__username', 'culture__name')
