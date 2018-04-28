from flask import Flask, render_template, jsonify
import pymysql

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
  static_folder = './dist/static',
  template_folder = './dist'
)

app.config.from_pyfile('config.cfg')

def connectDb():
  return pymysql.connect(
    host        = 'localhost',
    user        = 'root',
    password    = 'kodai1209',
    db          = 'shared_space',
    charset     = 'utf8mb4',
    cursorclass = pymysql.cursors.DictCursor
  )

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/api/files', methods=['GET'])
def fetchAllFileData():
  dbh = connectDb()
  cursor = dbh.cursor()
  sql = 'select f.id as id, data, '\
    'title, u.name as author, '\
    'f.created_at as created_at '\
    'from files as f join users as u '\
    'on f.uploader_id = u.id'
  cursor.execute(sql)
  files = cursor.fetchall()
  cursor.close()
  dbh.close()

  return jsonify(files)

if __name__ == '__main__':
  app.run(debug=True)
