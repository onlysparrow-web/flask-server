from flask import Flask, render_template
  
app = Flask(__name__) 

@app.route("/")
def home():
    return "Welcome"

@app.route("/debug/<username>")
def debug(username):
    return render_template("nav.html",username=username)

@app.route("/index/<user>")
def index(user):
    return render_template("index.html",user=user)


if __name__=="__main__":
    app.run(debug=True)

  