
import requests
from django.shortcuts import render

from .models import Ciudad
from .forms import CiudadForm


def index(request):

    url='http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&lang=es&appid=7d8f2370c0200fe8d32d5473de95206b'
    

    if request.method=='POST':

    	form=CiudadForm(request.POST)
    	form.save()

    form=CiudadForm()

    ciudades=Ciudad.objects.all()
    
    tiempo_datos=[]
    
    for ciudad in ciudades:
    	
    	tiempo_ciudad=requests.get(url.format(ciudad)).json()
    	
    	tiempo={
    		'ciudad':ciudad,
    		'temperatura':tiempo_ciudad['main']['temp'],
    		'descripcion':tiempo_ciudad['weather'][0]['description'],
    		'icono':tiempo_ciudad['weather'][0]['icon'],
    	}
    	tiempo_datos.append(tiempo)
    



    contexto={'tiempo_datos':tiempo_datos,'form':form}
    
    return render(request,'index.html',contexto)
