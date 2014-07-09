from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^invitationPrinter/', include('invitationPrinter.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Admin
    url(r'^admin/', include(admin.site.urls)),
    # ContactsManagement index
    url(r'^contactsmanagement/$', 'ContactsManagement.views.index'),
    # ContactsManagement Get contacts
    url(r'^contactsmanagement/getallcontacts$', 'ContactsManagement.views.getAllContacts'),
)