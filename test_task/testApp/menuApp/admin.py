from django.contrib import admin
from menuApp.models import MenuItem
from menuApp.forms import MenuItemForm


class MenuItemInline(admin.StackedInline):
    model = MenuItem
    form = MenuItemForm


class MenuItemAdmin(admin.ModelAdmin):
    inlines = [MenuItemInline]
    form = MenuItemForm

admin.site.register(MenuItem, MenuItemAdmin)