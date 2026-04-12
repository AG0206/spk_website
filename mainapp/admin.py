from django.contrib import admin
from django.utils.html import format_html
from .models import Event, Gallery, Contact


# ─────────────────────────────────────────────────────────────
# EVENT ADMIN
# ─────────────────────────────────────────────────────────────
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display  = ('thumb', 'title', 'badge', 'date_label', 'location',
                     'is_featured', 'is_active', 'order')
    list_editable = ('is_featured', 'is_active', 'order')
    list_filter   = ('badge', 'is_featured', 'is_active')
    search_fields = ('title', 'description', 'location')
    ordering      = ('order', '-created_at')
    list_per_page = 20

    fieldsets = (
        ('Basic Info', {
            'fields': ('title', 'description', 'image')
        }),
        ('Display Options', {
            'fields': ('badge', 'date_label', 'location', 'link_label')
        }),
        ('Visibility', {
            'fields': ('is_featured', 'is_active', 'order'),
            'description': 'Control how and where this event appears on the website.'
        }),
    )

    def thumb(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width:60px;height:44px;object-fit:cover;'
                'border-radius:4px;border:1px solid #e0e0e0;" />',
                obj.image.url
            )
        return format_html(
            '<div style="width:60px;height:44px;background:#c5e3ef;border-radius:4px;'
            'display:flex;align-items:center;justify-content:center;font-size:11px;color:#666;">No img</div>'
        )
    thumb.short_description = 'Image'


# ─────────────────────────────────────────────────────────────
# GALLERY ADMIN
# ─────────────────────────────────────────────────────────────
@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display  = ('thumb', 'title', 'category', 'size', 'is_active', 'order')
    list_editable = ('category', 'size', 'is_active', 'order')
    list_filter   = ('category', 'size', 'is_active')
    search_fields = ('title',)
    ordering      = ('order', '-created_at')
    list_per_page = 24

    fieldsets = (
        ('Image', {
            'fields': ('title', 'image')
        }),
        ('Display Options', {
            'fields': ('category', 'size', 'order', 'is_active'),
            'description': (
                'Category controls the filter tab. '
                'Size controls the grid cell: Normal=1×1, Large=2×1, Tall=1×2.'
            )
        }),
    )

    def thumb(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width:70px;height:50px;object-fit:cover;'
                'border-radius:4px;border:1px solid #e0e0e0;" />',
                obj.image.url
            )
        return '—'
    thumb.short_description = 'Preview'


# ─────────────────────────────────────────────────────────────
# CONTACT ADMIN
# ─────────────────────────────────────────────────────────────
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display  = ('name', 'email', 'phone', 'subject', 'is_read', 'created_at')
    list_editable = ('is_read',)
    list_filter   = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('name', 'email', 'phone', 'subject', 'message', 'created_at')
    ordering      = ('-created_at',)
    list_per_page = 30
    date_hierarchy = 'created_at'

    fieldsets = (
        ('Sender Details', {
            'fields': ('name', 'email', 'phone')
        }),
        ('Message', {
            'fields': ('subject', 'message', 'created_at')
        }),
        ('Status', {
            'fields': ('is_read',)
        }),
    )

    def has_add_permission(self, request):
        # Contact messages should only come from the website form
        return False
