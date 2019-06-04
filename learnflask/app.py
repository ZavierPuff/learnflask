from flask import Flask,request,send_from_directory,render_template

app = Flask(__name__)


@app.route('/hello')
def hello_world():
    return 'Hello World!'


@app.route('/blog/<string:blog_id>')
def show_blog_with_para( blog_id ):
    """
    flask define route string int float path uuid

    :param post_id:
    :return:
    """
    keyword = request.args.get('keyword', '')
    enc = request.args.get('enc', '')
    rel = ""
    if keyword:
        rel = rel+"key:" + keyword
    if enc:
        rel = rel + "en:" +enc
    return rel+ " Blog " + str(blog_id)


@app.route('/static/<path:path>')
def send_file(path):
    return send_from_directory('static',path)


@app.route('/html/hello')
def html_hello():
    return ''


@app.route('/html/hello')
def html_hello():
    return ''


if __name__ == '__main__':
    app.run()
