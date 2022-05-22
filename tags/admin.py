from django.contrib import admin
from tags.models import Tag

# Register your models here.


@admin.register(Tag)
class TaggedAdmin(admin.ModelAdmin):
    search_fields = ['label']