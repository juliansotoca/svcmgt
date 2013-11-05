#encoding:utf-8
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'serviceManager.views.home', name='home'),
    # url(r'^serviceManager/', include('serviceManager.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','svcmgt.views.lista_servicios'),
    url(r'^servicio/(?P<id_servicio>\d+)$','svcmgt.views.desc_servicio'),
)
