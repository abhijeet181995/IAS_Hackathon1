import random
import json
import time
import threading

class sensorClass:
    def __init__(self,id,stype,location,output_type,output_rate):
        self.data=[]
        self.sensor_id = id
        self.sensor_type = stype
        self.sensor_location = location
        self.output_type = output_type
        self.output_rate = output_rate
        threading.Thread(target=self.generate_data).start()

    def generate_data(self):
        while True:
            self.data.append(random.randint(1,10))
            time.sleep(self.output_rate)

    def get(self):
        return self.data
        self.data = []

with open("./app_repo/test/sensor_config.json","r") as fp:
    config = json.loads(fp.read())

sensor_object = {}

for sensor in config['Sensor']:
    sensor_object[sensor["Sensor_id"]] =  sensorClass(sensor['Sensor_id'],sensor["Sensor_type"],sensor["Sensor_location"],sensor["Sensor_output_type"],sensor["Sensor_output_rate"])

