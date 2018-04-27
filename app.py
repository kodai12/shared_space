from flask import Flask
from flask import render_template

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

@app.route('/')
def index():
  return render_template('index.html')
