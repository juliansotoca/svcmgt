#encoding:utf-8
from django.db import models

# Create your models here.

class Servicios(models.Model):
	idsvc = models.AutoField(primary_key=True)
	servicio = models.CharField(max_length=50, verbose_name='Título', unique=True)
	descripcion = models.TextField(verbose_name='Descripción', help_text='Descripción del servicio')
	
	def __unicode__(self):
		return self.servicio


class frontales(models.Model):
	H='HI'
	M='ME'
	L='LO'
	PRIORITIES_CHOICES=( (H, 'High'), (M, 'Medium'), (L, 'Low'))
	idfrontal = models.AutoField(primary_key=True)
	frontal = models.CharField(max_length=50, unique=True)
	servicio = models.ForeignKey(Servicios)
	prioridad = models.CharField(max_length=2, choices=PRIORITIES_CHOICES, default=M)
	
	def __unicode__(self):
		return self.frontal
	
class backends(models.Model):
	idbackend = models.AutoField(primary_key=True)
	backend = models.CharField(max_length=50, unique=True)
	servicio = models.ForeignKey(Servicios)
	
	def __unicode__(self):
		return self.backend
	
class baseDatos(models.Model):
	H='HI'
	M='ME'
	L='LO'
	PRIORITIES_CHOICES=( (H, 'High'), (M, 'Medium'), (L, 'Low'))
	idbbdd = models.AutoField(primary_key=True)
	bbdd = models.CharField(max_length=50, unique=True)
	backendProd = models.ForeignKey(backends, related_name='prodServer')
	backendBck = models.ForeignKey(backends, related_name='StandbyServer')
	prioridad = models.CharField(max_length=2, choices=PRIORITIES_CHOICES, default=M)
	
	def __unicode__(self):
		return self.bbdd
	
	
class aplicaciones(models.Model):
	idaplicacion = models.AutoField(primary_key=True)
	aplicacion = models.CharField(max_length=50, unique=True)
	servicio = models.ForeignKey(Servicios)
	
	def __unicode__(self):
		return self.aplicacion
