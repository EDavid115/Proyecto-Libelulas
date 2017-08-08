#Esta sería la función vista para "views.py" la cual llamarás al presionar un botón
#y te redirecciona a la página 'raspimediapp/publicar.html'

def publicar(request):
    os.system('pkill mosquitto_pub')
    comando = 'mosquitto_pub -h 192.168.1.13 -m "0" -t mensaje'
    os.system(comando)
    return render_to_response('raspimediapp/publicar.html')


#Este es el código que cargarás en el ESP

def recibir(request):
    os.system('pkill mosquitto_sub')
    comando = 'mosquitto_sub -h 192.168.1.13 -t mensaje'
    os.system(comando)
    return render_to_response('raspimediapp/recibir.html')
