from django.shortcuts import render
import paho.mqtt.subscribe as subscribe

# Create your views here.
def register(request):
	return render(request, 'registro.html')

def completeregis(request):
	return render(request, 'registrocompleto.html')
	# msg = subscribe.simple("uid", hostname="192.168.43.146")
	# data = msg.payload
	# if data is not None:
	# 	return render(request, 'registrocompleto.html', {'uid': data})
	# else:
	# 	return HttpResponse('Por favor coloca tu carné en el lector')
