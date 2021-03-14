import zipfile
import os
import shutil
import json
import jsonschema

app_config_schema={
    "type":"object",
    "properties":{
        "App_name":{
            "type":"string"
        },
        "Dependencies":{
            "type":"array",
            "items":{
                "type":"string"
            }
        },
        "Sensors":{
            "type":"array",
            "items":{
                "type":"number"
            }
        },
        "Sensor_config":"string"
    }
}

sensor_config_schema={
    "type":"object",
    "properties":{
        "Sensors":{
            "type":"array",
            "items":{
                "$ref":"#/$defs/sensor" 
            }
        }
    },
    "$defs":{
        "sensor":{
            "type":"object",
            "required":["Sensor_id","Sensor_location","Sensor_type","Sensor_output_type","Sensor_output_rate"],
            "properties":{
                "Sensor_id":{
                    "type":"number"
                },
                "Sensor_location":{
                    "type":"string"
                },
                "Sensor_type":{
                    "type":"string"
                },
                "Sensor_output_type":{
                    "type":"string"
                },
                "Sensor_output_rate":{
                    "type":"number"
                },
            }
        }
    },
}

app_repo='app_repo/'

def validate_sensor_config(json_path):
    with open(json_path,'r') as fp:
        sensor_json=json.load(fp)
    print(sensor_json)
    jsonschema.validate(sensor_json,schema=sensor_config_schema)

def validate_app(zip_path):
    #print(zip_path)
    with zipfile.ZipFile(zip_path,'r') as zip:
        zip.extractall('./temp/')
    file_name=zip_path.split('/')[-1].split('.')[:-1]
    file_name=''.join(file_name)
    if os.path.exists('./temp/'+file_name):
        with open('./temp/'+file_name+'/app_config.json','r') as fp:
            app_json=json.load(fp)
        jsonschema.validate(app_json,app_config_schema)
        validate_sensor_config('./temp/'+file_name+'/sensor_config.json')
        shutil.move('./temp/'+file_name,app_repo+file_name)
    pass



