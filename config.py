import os

debug = True
SECRET_KEY = os.urandom(24)
DB_ROOT = 'root'
DB_PWD = 'root'
DB_HOST = 'localhost'
DB_NAME = 'zlbbs'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://%s:%s@%s/%s' % (DB_ROOT, DB_PWD
                                                           , DB_HOST, DB_NAME)
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_COMMIT_ON_TEARDOWN = True

CMS_USER_ID = 'fsdfasfasfa'
FRONT_USER_ID = 'fsdfasfasf'

# 邮箱
MAIL_SERVER = "smtp.qq.com"
MAIL_PORT = "587"
MAIL_USE_TLS = True
MAIL_USERNAME = "2310308583@qq.com"
MAIL_PASSWORD = "uwpnnfexuowkebah"
MAIL_DEFAULT_SENDER = "2310308583@qq.com"

# 阿里大于相关配置
ALIDAYU_APP_KEY = 'LTAI4GEAa9cHq88oEGdahuCD'
ALIDAYU_APP_SECRET = 'Hb8SsROuwHMN7g7xZH78933QqqtUa3'
ALIDAYU_SIGN_NAME = '知了论坛'
ALIDAYU_TEMPLATE_CODE = 'SMS_189523758'


UEDITOR_UPLOAD_PATH = os.path.join(os.path.dirname(__file__), 'images')

#flask-paginate
PER_PAGE = 10


# celery相关的配置
CELERY_RESULT_BACKEND = "redis://127.0.0.1:6379/0"
CELERY_BROKER_URL = "redis://127.0.0.1:6379/0"
