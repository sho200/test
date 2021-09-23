from flask import Flask, request, abort
import logging
import sys

app = Flask(__name__)
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.INFO)

@app.route('/')
def top_page():
    return 'Here is root page.'

@app.route('/callback', methods=['POST'])
def callback_post():

    return 'OK'

if __name__ == '__main__':
    app.run()
