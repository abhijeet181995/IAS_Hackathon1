import subprocess
import threading

def read_data(process,app_path):
    while True:
        data=process.stdout.read()
        with open(app_path+'/output.txt','wb') as f:
            f.write(data)

def execute(app_path):
    process=subprocess.Popen(['python3',app_path+'/init.py'],stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    thread=threading.Thread(target=read_data,args=(process,app_path))
    thread.start()
    thread.join()

execute('./app_repo/test')