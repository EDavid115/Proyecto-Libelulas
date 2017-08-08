import mfrc522
import time
from os import uname
from umqtt.simple import MQTTClient


def do_read():

	if uname()[0] == 'WiPy':
		rdr = mfrc522.MFRC522("GP14", "GP16", "GP15", "GP22", "GP17")
	elif uname()[0] == 'esp8266':
		rdr = mfrc522.MFRC522(0, 2, 4, 5, 14)
	else:
		raise RuntimeError("Unsupported platform")

	print("")
	print("Place card before reader to read from address 0x08")
	print("")

	try:
		while True:

			(stat, tag_type) = rdr.request(rdr.REQIDL)

			if stat == rdr.OK:

				(stat, raw_uid) = rdr.anticoll()

				if stat == rdr.OK:
					print("New card detected")
					print("  - tag type: 0x%02x" % tag_type)
					print("  - uid	 : 0x%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3]))
					print("")
					newuid = (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3])

					if rdr.select_tag(raw_uid) == rdr.OK:

						key = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]

						if rdr.auth(rdr.AUTHENT1A, 8, key, raw_uid) == rdr.OK:
							print("Address 8 data: %s" % rdr.read(8))
							rdr.stop_crypto1()
						else:
							print("Authentication error")
					else:
						print("Failed to select tag")
					return newuid
	except KeyboardInterrupt:
		print("Bye")

def pub_data(data):
	# Test reception e.g. with:
	# mosquitto_sub -t foo_topi
    c = MQTTClient("umqtt_client", "192.168.1.5")
    c.connect()
    c.publish("uid", data)
    c.disconnect()

try:
	while True:
		card = []
		card = do_read()
		print (card)
		data = str(card)
		time.sleep(1)
		if card != []:
			dato = str(card)
			pub_data(dato)
			card = []
			time.sleep(1)
except KeyboardInterrupt:
			print("Bye")
