from django.contrib import admin
from .models import Car
from main.admin import ImageElementInline

# Register your models here.

# admin.site.register(Cars)


class CarAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Dane samochodu", {'fields': ['title', 'description']}),
    ]
    inlines = [ImageElementInline]


admin.site.register(Car, CarAdmin)
