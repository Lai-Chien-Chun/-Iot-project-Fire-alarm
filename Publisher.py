# Publisher.py
import paho.mqtt.client as mqtt

_g_cst_ToMQTTTopicServerIP = "192.168.7.4"
_g_cst_ToMQTTTopicServerPort = 1883 #port
_g_cst_MQTTTopicName = "BBGW" #TOPIC name

mqttc = mqtt.Client("python_pub")
mqttc.connect(_g_cst_ToMQTTTopicServerIP, _g_cst_ToMQTTTopicServerPort)
mqttc.publish(_g_cst_MQTTTopicName, "Hello")