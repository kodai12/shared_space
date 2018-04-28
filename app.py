from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy

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

app = CustomFlask(__name__,
                  static_folder = './dist/static',
                  template_folder = './dist')

app.config.from_pyfile('config.cfg')

db = SQLAlchemy(app)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/api/file_data/<int:file_id>')
def fetchFile(file_id):
