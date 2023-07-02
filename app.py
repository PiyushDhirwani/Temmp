from flask import Flask
from checkinterface.implementation import Implementation

app = Flask(__name__)

@app.route('/')
def hello_world():
    obj = Implementation()
    result = obj.some_function(5,10)
    return result

if __name__ == '__main__':
    app.run()