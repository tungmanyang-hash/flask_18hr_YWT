from flask import Flask


app = Flask(__name__)

#----------practice start------------
@app.route('/')
def index():
    return '<h1>!@#$Bad Request!!!!</h1>', 502, {"key1":103, "key2":301}
#----------practice end--------------

if __name__ == '__main__':
    app.run(debug=True)
