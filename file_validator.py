import zipfile

def validate_app(zip_path):
    print(zip_path)
    with zipfile.ZipFile(zip_path,'r') as zip:
        zip.extractall('./temp/'+zip_path.split('/')[-1])
    
    pass

validate_app(input())