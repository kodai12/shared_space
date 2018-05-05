from flask import Flask, render_template, jsonify, request
import configparser
import werkzeug
from datetime import datetime
import os
from flask_httpauth import HTTPDigestAuth
from models import fetchUsers, fetchAllFileData, saveUploadedFile


# create custom flask instance
class CustomFlask(Flask):
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
        block_start_string='(%',
        block_end_string='%)',
        variable_start_string='((',
        variable_end_string='))',
        comment_start_string='(#',
        comment_end_string='#)',
    ))


app = CustomFlask(
    __name__,
    static_folder='./dist/static',
    template_folder='./dist'
)

# read config file
config = configparser.SafeConfigParser()
config.read('config.cfg')

# file upload settings
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024
UPLOAD_DIR = './static/files'

# auth settings
app.config['SECRET_KEY'] = 'test'
auth = HTTPDigestAuth()
users = fetchUsers()


@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None


# route settings
# ルーティング処理はVueRouterで制御するのでflask側では全てのリクエストにて対しindex.htmlを返す
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
@auth.login_required
def index(path):
    return render_template('index.html')


# api settings
@app.route('/api/files', methods=['GET'])
def getAllFileData():
    files = fetchAllFileData()
    return jsonify(files)


@app.route('/api/file', methods=['POST'])
def uploadFile():
    if 'uploadFile' not in request.files:
        return 'result: uploadFile is required.'

    file = request.files['uploadFile']
    fileName = file.filename
    if '' == fileName:
        return 'result: fileName must not empty.'

    saveFileName = datetime.now().strftime('%Y%m%d_%H%M%S_') \
        + werkzeug.utils.secure_filename(fileName)
    saveFilePath = os.path.join(UPLOAD_DIR, saveFileName)
    file.save(saveFilePath)
    saveUploadedFile(saveFilePath)
    return 'result: upload is succeeded.'


@app.errorhandler(werkzeug.exceptions.RequestEntityTooLarge)
def handle_over_max_file_size(error):
    print('werkzeug.exceptions.RequestEntityTooLarge')
    return 'result: file size is too large.'


@app.route('/api/login-user', methods=['GET'])
def fetchLoginUser():
    return 'sakochi'


if __name__ == '__main__':
    app.run(debug=True)
