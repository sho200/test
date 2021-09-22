from flask import Flask, request, abort


app = Flask(__name__)
# 必須ではないけれど、サーバに上がったとき確認するためにトップページを追加しておきます。
@app.route('/')
def top_page():
    return 'Here is root page.'

if __name__ == '__main__':
    app.run()
