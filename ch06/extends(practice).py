from flask import Flask, render_template


app = Flask(__name__)



#----------practice start------------
@app.route('/')
def index():
    return render_template("basic_extends(practice).html", page_header = "Page header")

@app.route('/block')
def block():
    return render_template("block(practice).html")

@app.route('/super')
def jinja2_super():
    return render_template("super(practice).html", page_header = "test super()")

#----------practice end-------------- 
#extend 可以限定繼承，include 只能原內容照搬，不能客製


if __name__=="__main__":
    app.run(debug=True)
