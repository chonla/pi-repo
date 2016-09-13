#!/usr/bin/env python

import picamera
import json
from datetime import datetime
import os

with open('pi-camera.json') as json_file:
    j = json.load(json_file)

output_folder = j['output']['folder']
output_prefix = j['output']['prefix']
file_name = output_prefix + datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + '.jpg'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

cam = picamera.PiCamera()
cam.capture(output_folder + '/' + file_name)
