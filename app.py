from flask import Flask
import os
port = int(os.environ.get('PORT'))

app=Flask(__name__)

@app.route("/")
def hello():
    return "Hey there whats up world we just deployed something and python is superiorrr!"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=port)