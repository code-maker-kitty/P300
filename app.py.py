from paho.mqtt import client as mqtt_client
from flask import Flask, render_template
import time

app = Flask(__name__)
def on_connect(client, userdata, flags, rc):
	client.subcribe("topicName/pir")
def on_message(client, userdata, msg):
	global detection
	detection = msg.payload.decode('utf8')
@app.route('/', methods=['GET'])
def check_detention():
	client = mqtt.Client()
	client.on_connect = on_connect
    client.on_message = on_message
    client.connect("broker.emqx.io", 1883)
    client.loop_start()
    for i in range(0,10):
    	time.sleep(5)
    	print('detection = ', detection)
    	return render_template('index.html', status = int(detection))
    client.loop_stop()
if __name__ == '__main__':
	app.run(port = 5001)