from flask import Flask, request, abort

app = Flask(__name__)
@app.route('/')
def top_page():
    return 'Here is root page.'

@app.route('/callback', methods=['POST'])
def callback_post():

    return 'OK'

if __name__ == '__main__':
    app.run()
