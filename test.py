from flask import Flask, request, abort
@app.route('/')
def top_page():
    return 'Here is root page.'

@app.route('/callback', methods=['POST'])
def callback_post():
    dt_now = datetime.datetime.now()
    t =dt_now.strftime('%Y年%m月%d日\n%H時%M分%S秒')
    return 'OK'

if __name__ == '__main__':
    app.run()
