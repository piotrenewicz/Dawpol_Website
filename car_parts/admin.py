from django.contrib import admin
from .models import Part
from main.admin import ImageElementInline

# Register your models here.

# admin.site.register(Cars)


class PartAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Nazwa_Części: ", {'fields': ['title', 'description']}),
    ]
    inlines = [ImageElementInline]


admin.site.register(Part, PartAdmin)
