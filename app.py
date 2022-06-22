ffrom flask import Flask
from flask import Response
from flask import render_template
import cv2
import numpy as np

app = Flask(__name__)


@app.route('/')
def index():
    #return render_template("index.html")
    
    matt = np.zeros(1280,720)
    cv2.imwrite("img.png", matt)
    return "This is the amazing app EVER, speaking at zf openshift."
 

@app.route("/healthz")
def healthz():
    resp = Response("ok")
    resp.headers['Custom-Header'] = 'Awesome'
    # this is awesome tying things
    return resp

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080')
