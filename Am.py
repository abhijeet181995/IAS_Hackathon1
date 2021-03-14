from flask import Flask ,request , render_template ,redirect , url_for 
import os
from file_validator import validate_app

app = Flask(__name__)

app.config['upload_extensions']=['zip','json']
app.config['upload_path']='temp'
UserList={

}


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
        try:
            validate_app(save_path)
        except:
            return "Wrong Format"
        return "File successfully uploaded"

@app.route("/",methods=["GET","POST"])
def index():
    if request.method=="POST":
        user = request.form['user']
        passwd = request.form['pass']
        if UserList[user] == passwd:
            return redirect(url_for('app_upload'))
        else:
            return redirect("/")
    return render_template("index.html")


@app.route("/signup",methods=["GET","POST"])
def signup():
    if request.method=="POST":
        user = request.form['user']
        passwd = request.form['pass']
        UserList[user] = passwd
        return redirect("/")
    return render_template("signup.html")

if __name__=="__main__":
    app.run(debug=True)
