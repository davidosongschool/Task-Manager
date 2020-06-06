import os
from flask import Flask
from os import path
if path.exists("env.py"):
    import env


app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello Flask'


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
