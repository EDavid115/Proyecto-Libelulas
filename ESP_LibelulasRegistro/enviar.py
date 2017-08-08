import paho.mqtt.publish as publish
import time

print("Enviando 0...")
publish.single("estado", "0")
time.sleep(1)
print("Enviando 1...")
publish.single("estado", "1")
