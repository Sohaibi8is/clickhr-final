from flask import Flask
app=Flask(__name__)
@app.route("/",methods=["GET","POST"]) 
def home():
    return"<h1>HEY SOHAIB</h1>"
if __name__=="__main__":
    app.run(port=443,host='0.0.0.0')
