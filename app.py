from flask import Flask, render_template, jsonify
import pymysql
import configparser

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
  static_folder = './dist/static',
  template_folder = './dist'
)

# read config file
config = configparser.SafeConfigParser()
config.read('config.cfg')

def connectDb():
  # 設定ファイルからDB接続情報を読み込み
  host = config.get('development', 'MYSQL_DATABASE_HOST')
  user = config.get('development', 'MYSQL_DATABASE_USER')
  password = config.get('development', 'MYSQL_DATABASE_PASSWORD')
  db = config.get('development', 'MYSQL_DATABASE_DB')

  return pymysql.connect(
    host = host,
    user = user,
    password = password,
    db = db,
    charset = 'utf8mb4',
    cursorclass = pymysql.cursors.DictCursor
  )

# route settings
@app.route('/')
def index():
  return render_template('index.html')

# api settings
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
