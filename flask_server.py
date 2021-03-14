from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="GET":
        return render_template('login.html')
    if request.method=="POST":
        print(request.form.to_dict())
        return 'Check'

@app.route("/")
@app.route("/index")
def root():
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True,port=8080)