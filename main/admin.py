from django.contrib import admin
from .models import TextContent, ImageListing, ImageElement, ImageContent, Page


# Register your models here.

admin.site.register(TextContent)
# admin.site.register(GraphicalItem)
admin.site.register(ImageContent)


class ImageElementInline(admin.TabularInline):
    model = ImageElement
    extra = 0


class ImageListingAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Nazwa_Bazy', {'fields': ['id']}),
    ]
    inlines = [ImageElementInline]


admin.site.register(ImageListing, ImageListingAdmin)


class PageAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'order')
    ordering = ('order', 'id')


admin.site.register(Page, PageAdmin)
