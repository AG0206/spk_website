from django.urls import path
from . import views

urlpatterns = [

    # ── Public pages ──
    path('',          views.home,        name='home'),
    path('about/',    views.about,       name='about'),
    path('events/',   views.events_page, name='events'),
    path('gallery/',  views.gallery_page,name='gallery'),
    path('contact/',  views.contact,     name='contact'),

    # ── Custom Admin Panel ──
    path('adminlogin/',  views.custom_admin_login,   name='custom_admin_login'),
    path('adminlogout/', views.custom_admin_logout,  name='custom_admin_logout'),

    path('adminpanel/',              views.custom_admin_dashboard, name='custom_admin_dashboard'),
    path('adminpanel/events/',       views.custom_admin_events,    name='custom_admin_events'),
    path('adminpanel/events/add/',   views.custom_admin_event_add, name='custom_admin_event_add'),
    path('adminpanel/events/<int:pk>/edit/',   views.custom_admin_event_edit,   name='custom_admin_event_edit'),
    path('adminpanel/events/<int:pk>/delete/', views.custom_admin_event_delete, name='custom_admin_event_delete'),

    path('adminpanel/gallery/',               views.custom_admin_gallery,        name='custom_admin_gallery'),
    path('adminpanel/gallery/<int:pk>/delete/', views.custom_admin_gallery_delete, name='custom_admin_gallery_delete'),

    path('adminpanel/contacts/',               views.custom_admin_contacts,           name='custom_admin_contacts'),
    path('adminpanel/contacts/export/',        views.custom_admin_contacts_export,    name='custom_admin_contacts_export'),
    path('adminpanel/contacts/<int:pk>/read/', views.custom_admin_contact_toggle_read, name='custom_admin_contact_toggle_read'),
    path('adminpanel/contacts/<int:pk>/delete/', views.custom_admin_contact_delete,   name='custom_admin_contact_delete'),
]
