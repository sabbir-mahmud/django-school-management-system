from django.contrib import admin
from .models import School, Section, Class, Subject

# Register your models here.


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'city', 'state',
                    'zip', 'phone', 'email', 'website')
    list_filter = ('name', 'address', 'city', 'state',
                   'zip', 'phone', 'email', 'website')
    search_fields = ('name', 'address', 'city', 'state',
                     'zip', 'phone', 'email', 'website')
    ordering = ('name', 'address', 'city', 'state',
                'zip', 'phone', 'email', 'website')
    filter_horizontal = ()
    filter_vertical = ()
    fieldsets = ()


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)
    ordering = ('name',)
    filter_horizontal = ()
    filter_vertical = ()
    fieldsets = ()


class SubjectInline(admin.TabularInline):
    model = Subject
    extra = 0


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)
    ordering = ('name',)
    filter_horizontal = ()
    filter_vertical = ()
    fieldsets = ()
    inlines = [SubjectInline]
