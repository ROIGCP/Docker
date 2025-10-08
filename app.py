from flask import Flask, request
from waitress import serve
from faker import Faker
import os
import logging
import random

app = Flask(__name__)
logger = logging.getLogger('waitress')
logger.setLevel(logging.DEBUG)
fake = Faker()

@app.route("/")
def getRoot():
  return "ROI Training Demo is working!\n"

@app.route("/headers")
def show_headers():
  client_ip = request.remote_addr
  user_agent = request.headers.get('User-Agent')
  referer = request.headers.get('Referer')
  accept_language = request.headers.get('Accept-Language')
  all_headers = dict(request.headers)
  header_info = f"Your IP address is: {client_ip}<br\>" \
                f"Headers: {all_headers}"
  return header_info

@app.route("/random")
def getRandom():
  randomnum = random.randint(1, 100000000)/100
  return "Your Random Number is " + str(randomnum) + "!\n"

@app.route("/name")
def getRandomName():
  randomname = "Welcome " + fake.name()
  return randomname

@app.route("/version")
def version():
  return "ROI Training Demo 1.0\n"

if __name__ == "__main__":
  serve(app,host="0.0.0.0",port=int(os.environ.get("PORT", 8080)))
