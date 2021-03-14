from flask import Flask ,request , render_template

app = Flask(__name__)

UserList={

}

@app.route("/",methods=["GET","POST"])
def index():
    if request.method=="POST":
        user = request.form['user']
        passwd = request.form['pass']
        if UserList[user] == passwd:
            return "Success"
        else:
            return "failed"
    return render_template("index.html")


@app.route("/signup",methods=["GET","POST"])
def signup():
    if request.method=="POST":
        user = request.form['user']
        passwd = request.form['pass']
        UserList[user] = passwd
    
    return render_template("signup.html")

if __name__=="__main__":
    app.run(debug=True)