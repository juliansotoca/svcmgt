#encoding:utf-8
# Create your views here.
from svcmgt.models import Servicios, frontales, backends, baseDatos, aplicaciones
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
import datetime
import json


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


def current_datetime(request):
	now = datetime.datetime.now()
	html="<html><body>It is now %s.</body></html>" % now
	return HttpResponse(html)

def get_full_tree(request):
	svc = Servicios.objects.all()
	app = aplicaciones.objects.all()
	fends = frontales.objects.all()
	bends = backends.objects.all()
	bbdd = baseDatos.objects.all()
	return render_to_response('tree.html', {'servicio':svc, 'aplicaciones':app, 'frontends':fends, 'backends':bends, 'baseDatos':bbdd})


def get_json(request):
	svc = Servicios.objects.all()
	app = aplicaciones.objects.all()
	fends = frontales.objects.all()
	bends = backends.objects.all()
	bbdd = baseDatos.objects.all()
	data={}
	fullJson=[]
	for s in svc:
		data['service'] = s.servicio
		_f=[]
		for f in fends:
			if f.servicio == s:
				_f.append(f.frontal)
		data['frondends'] = _f
		_a=[]
		for a in app:
			if a.servicio == s:
				_a.append(a.aplicacion)
		data['aplicaciones'] = _a
		_b=[]
		_d=[]
		for b in bends:
			if b.servicio == s:
				_b.append(b.backend)
				for d in bbdd:
					if d.backendProd == b:
						_d.append(d.bbdd)
		data['backends'] = _b
		data['bbdd'] = _d
		fullJson.append(data.copy())
		
	html="<html><body>%s</body></html>" % json.dumps(fullJson, sort_keys=True, indent=2)
	return HttpResponse(html)
