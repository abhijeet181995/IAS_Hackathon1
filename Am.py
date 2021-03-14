from flask import *
import os
from file_validator import validate_app

app=Flask(__name__)

app.config['upload_extensions']=['zip','json']
app.config['upload_path']='temp'
UserList=dict()

@app.route("/app_upload",methods=["GET","POST"])
def app_upload():
    if request.method=="GET":
        return render_template('app_upload.html')
    if request.method=="POST":
        #print(request)
        file_received=request.files['app_file']
        print(file_received.filename)
        if not os.path.exists('temp'):
            os.mkdir('temp')
        save_path=os.path.join(app.config['upload_path'],file_received.filename)
        file_received.save(save_path)
    validate_app(save_path)
    return "File successfully uploaded"

@app.route("/")
@app.route("/index")
def index():
    if request.method=="POST":
        user = request.form['user']
        passwd = request.form['pass']
        if UserList[user] == passwd:
            return redirect(url_for('app_upload'))
        else:
            return "failed"
    return render_template("index.html")

if __name__=="__main__":
    print("check")
    app.run(debug=True,port=8080)
