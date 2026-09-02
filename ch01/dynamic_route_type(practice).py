from flask import Flask
from markupsafe import escape


app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

# ----------practice start------------
@app.route('/user/<name>/<int:id_>')  #int: 可以改成 float:(但網址輸入處數字部分要.0) 或 str:
def user_check_type(name, id_):
    return (f'<h1>id: {id_}!</h1>'
            f'<h1>name: {name}!</h1>'
            f'<h1>id type: {escape(type(id_))}!</h1>'
            f'<h1>name type: {escape(type(name))}!</h1>')
# ----------practice end--------------

if __name__ == '__main__':
    app.run(debug=True)
