import sys
import time
import paho.mqtt.publish as publish
import Adafruit_BBIO.GPIO as GPIO
import mraa
val = mraa.Aio(1)
GPIO.setup("P9_22",1)
channelID = "648794"
apiKey = "HC76WITLEXSUMF0G"
mqttHost = "mqtt.thingspeak.com"
useSSLWebsockets = True
fire=0
if useSSLWebsockets:
    import ssl
    tTransport = "websockets"
    tTLS = {'ca_certs':"/etc/ssl/certs/ca-certificates.crt",'tls_version':ssl.PROTOCOL_TLSv1}
    tPort = 443       
topic_fire = "channels/" + channelID + "/publish/" + apiKey
while True:
	#fire sensor
	#print(GPIO.input("P9_22"))
	if GPIO.input("P9_22"):
		print("detect fire")
		fire=1
	else:
		print("no fire")
		fire=0
	valr=val.read()
	#print(valr)
	v=(valr/1024.0)*1.8
	#print(v)
	ppm=300+9700/4*v-2000
	if ppm<2000:
		print 'save ppm: ',int(ppm)
	else:
		print 'detect gas!! ppm: ',int(ppm)
	##tPayload=str(topic_fire)
	tPayload = "field4=" + str(ppm) + "&field3=" + str(fire)
	#tPayload = "field3=" + str(fire)
	publish.single(topic_fire, payload=tPayload, hostname=mqttHost, port=tPort, tls=tTLS, transport=tTransport)
	time.sleep(1)
	
