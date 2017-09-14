from app import app

SECRET_KEY = '$5$rounds=535000$O/od5B7GUkTCkcG.$7U6jJ6QnLvyJo8NkAch7KWfwMrPKolfzwtYJOq/7JQ5'
DEBUG = True

# Config MySQL
MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = '123456'
MYSQL_DB = 'flastweet'
MYSQL_CURSORCLASS = 'DictCursor'