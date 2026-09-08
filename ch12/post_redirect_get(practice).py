# practice start
from flask import Flask, render_template, request, redirect, url_for, session

# practice end

from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',
                           page_header="page_header",
                           current_time=datetime.utcnow())

# practice start
<form method="POST" action="{{request.full_path}}">
# practice 


if __name__ == "__main__":
    app.run(debug=True)
