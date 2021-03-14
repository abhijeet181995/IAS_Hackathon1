import zipfile
import os
import shutil
import json
import jsonschema

app_config_schema={
    "type":"object",
    "properties":{
        "app_name":{
            "type":"string"
        },
        "sensors":{
            "type":"array",
            "items":{
                "type":"number"
            }
        },
        "dependencies":{
            "type":"array",
            "items":{
                "type":"string"
            }
        },
        "scheduling":{
            "type":"object",
            "properties":{
                "start_time":{
                    "type":"number"
                },
                "end_time":{
                    "type":"number"
                },
                "job_type":{
                    "type":"string"
                },
            }
        }
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

app_repo='./app_repo/'

def validate_sensor_config(json_path):
    with open(json_path,'r') as fp:
        sensor_json=json.load(fp)
    jsonschema.validate(sensor_json,schema=sensor_config_schema)

def validate_app(zip_path):
    file_name=zip_path.split('/')[-1].split('.')[:-1]
    file_name=''.join(file_name)

    with zipfile.ZipFile(zip_path,'r') as zip:
        if len(zip.infolist())>1:
            zip.extractall('./temp/'+file_name+'/')
        else:
            zip.extractall('./temp/')
    
    if os.path.exists('./temp/'+file_name):
        with open('./temp/'+file_name+'/app_config.json','r') as fp:
            app_json=json.load(fp)
        try:
            jsonschema.validate(app_json,app_config_schema)
            validate_sensor_config('./temp/'+file_name+'/sensor_config.json')
        except:
            shutil.rmtree('./temp/'+file_name)
            return False,None
        shutil.move('./temp/'+file_name,app_repo+file_name)
        os.remove(zip_path)
    return True,app_repo+file_name