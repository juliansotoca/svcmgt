#encoding:utf-8
from svcmgt.models import Servicios, frontales, backends, baseDatos, aplicaciones
from django.contrib import admin
admin.site.register(Servicios)
admin.site.register(frontales)
admin.site.register(backends)
admin.site.register(baseDatos)
admin.site.register(aplicaciones)
