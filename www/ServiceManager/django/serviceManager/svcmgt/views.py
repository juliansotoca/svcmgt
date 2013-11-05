#encoding:utf-8
# Create your views here.
from svcmgt.models import Servicios, frontales, backends, baseDatos, aplicaciones
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404

def lista_servicios(request):
	svc = Servicios.objects.all()
	return render_to_response('lista_servicios.html', {'lista':svc})

def desc_servicio(request, id_servicio):
	dato = get_object_or_404(Servicios, pk=id_servicio)
	svc = Servicios.objects.get(idsvc=id_servicio).servicio
	app = aplicaciones.objects.filter(servicio=id_servicio)
	fends = frontales.objects.filter(servicio=id_servicio)
	bends = backends.objects.filter(servicio=id_servicio)
	bbdd = baseDatos.objects.filter(backendProd=bends)
	return render_to_response('descripcion_servicio.html', {'servicio':svc, 'aplicaciones':app, 'frontends':fends, 'backends':bends, 'baseDatos':bbdd})
