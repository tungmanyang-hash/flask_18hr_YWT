#----------practice start------------
from flask import Flask, make_response
#----------practice end--------------

app = Flask(__name__)

#----------practice start------------
@app.route('/')
def index():
    response = make_response('<h1>Check the status code</h1>')
    response.status_code = 402
    print("response.content_length :",response.content_length,  
          "len(\"<h1>Check the status code</h1>\"):",len("<h1>Check the status code</h1>"))
    return response
#----------practice end--------------
#response.content_length可檢驗回傳的內容的長度(會顯示在 cmd)


if __name__ == '__main__':
    app.run(debug=True)
