from flask import Flask, render_template
  
app = Flask(__name__) 

items=[{"id":1,"name":"iphone","price":50000,"description":"Iphone x"},
{"id":2,"name":"samsung","price":40000,"description":"samsung ultraedge"},
{"id":3,"name":"redmi","price":20000,"description":"note 7 pro"}, 
{"id":4,"name":"nothing","price":20000,"description":"nothing pro x"},
{"id":5,"name":"lg","price":30000,"description":"dual pro rgx"}]
@app.route("/")
def home():
    return "Welcome"

@app.route("/debug/<username>")
def debug(username):
    return render_template("nav.html",username=username)

@app.route("/index/<user>")
def index(user):
    return render_template("index.html",user=user,len=len(items),items=items)


if __name__=="__main__":
    app.run(debug=True)

  