from django.contrib import admin
from .models import Content, GraphicalItemManager, GraphicalItem


# Register your models here.

admin.site.register(Content)
admin.site.register(GraphicalItemManager)
admin.site.register(GraphicalItem)

