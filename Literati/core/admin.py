from django.contrib import admin
from .models import Service, ContactMessage

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('category', 'title')
    list_filter = ('category',)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')


    from django.contrib import admin
from .models import Page, ContactMessage

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('page_name', 'title')


