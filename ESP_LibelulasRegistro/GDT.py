import paho.mqtt.subscribe as subscribe

msg = subscribe.simple("uid", hostname="192.168.1.5")
print("%s %s" % (msg.topic, msg.payload))
dat = msg.payload
print(dat)
