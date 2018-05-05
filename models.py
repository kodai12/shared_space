import pymysql
import configparser

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
        host=host,
        user=user,
        password=password,
        db=db,
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )


def fetchUsers():
    connection = connectDb()
    try:
        with connection.cursor() as cursor:
            sql = 'select name, password from users'
            cursor.execute(sql)
            users = cursor.fetchall()
            connection.commit()
            cursor.close()
    finally:
        connection.close()

    if users:
        user_infos = {}
        for i in range(len(users)):
            user_name = users[i]['name']
            user_password = users[i]['password']
            user_infos[user_name] = user_password

        return user_infos


def fetchAllUsers():
    connection = connectDb()
    try:
        with connection.cursor() as cursor:
            sql = 'select name, password from users'
            cursor.execute(sql)
            users = cursor.fetchall()
            connection.commit()
            cursor.close()
    finally:
        connection.close()
    return users


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

    return files


def saveUploadedFile(saveFilePath):
    connection = connectDb()
    try:
        with connection.cursor() as cursor:
            sql = 'insert into files(data, title, uploader_id)' \
                ' values(%s, %s, %s)'
            cursor.execute(sql, (saveFilePath, 'test', 1))
            connection.commit()
            cursor.close()
    finally:
        connection.close()
