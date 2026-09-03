from flask import Flask, render_template


app = Flask(__name__)



#----------practice start------------
@app.route('/')
def index():
    return render_template("basic_extends(practice).html", page_header = "Page header")
#----------practice end-------------- 


if __name__=="__main__":
    app.run(debug=True)
