from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "<h1 style='text-align: center;'>Welcome to Udacity Cloud DevOps Engineer Nanodegree Capstone Project!</h1><p>Written by Gökhan Özkan</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True) # specify port=80
