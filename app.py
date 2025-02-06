from typing import TypeVarTuple
from flask import Flask

app = Flask(__name__)
@app.route("/")
def hello_world ():
    return "python with flask"
if __name__ == "__main__":
   app.run(host='0.0.0.0', debug=True)