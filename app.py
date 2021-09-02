from flask import Flask
from waitress import serve
import os
import logging
import random

app = Flask(__name__)
logger = logging.getLogger('waitress')
logger.setLevel(logging.DEBUG)

@app.route("/")
def hello():
  randomnum = random.randint(1, 100000000)/100
  return "Your Random Number is " + str(randomnum) + "!\n"

@app.route("/version")
def version():
  return "ROIGCP Demo 1.0\n"

if __name__ == "__main__":
  serve(app,host="0.0.0.0",port=int(os.environ.get("PORT", 8080)))
