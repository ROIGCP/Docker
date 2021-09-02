from flask import Flask
from waitress import serve
import os

import random

app = Flask(__name__)

@app.route("/")
def hello():
  acct_balance = random.randint(1, 100000000)/100
  return "Your Bank Account Balance is $" + str(acct_balance) + "!\n"

@app.route("/version")
def version():
  return "Helloworld 1.1\n"

if __name__ == "__main__":
  serve(app,host="0.0.0.0",port=int(os.environ.get("PORT", 8080)))
