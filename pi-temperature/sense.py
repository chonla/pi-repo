#!/usr/bin/env python3

import Adafruit_DHT
import requests
import json
import os

cwd = os.path.dirname(os.path.realpath(__file__))

with open('{0}/pi-camera.json'.format(cwd)) as json_file:
    j = json.load(json_file)

url = j['repository']['url']

# Sensor should be set to Adafruit_DHT.DHT11,
# Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.
sensor = Adafruit_DHT.AM2302

# Example using a Raspberry Pi with DHT sensor
# connected to GPIO23.
pin = 4

# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
if humidity is not None and temperature is not None:
    print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
    r = requests.post(url, data={'temp': temperature, 'humid': humidity})
    print('Status:{0}'.format(r.status_code))
else:
    print('Failed to get reading. Try again!')