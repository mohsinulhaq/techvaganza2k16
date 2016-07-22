DEBUG = True
SECRET_KEY = 'FsdfswsskfhAOCABSKJFNAKdfbgfgaJCNWOACNQWIKXNxbcqcnskjcnIUH287R2YRHI2132FVJBKVBJSVB'
SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/tv_db'
SQLALCHEMY_TRACK_MODIFICATIONS = True  # Just to suppress warnings.

# For flask
UPLOAD_FOLDER = '/tmp'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'doc', 'docx'}

# For flask debug toolbar.
DEBUG_TB_INTERCEPT_REDIRECTS = False

# For pagination
RESULTS_PER_PAGE = 5

# For mail
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'techvaganza2k16@gmail.com'
MAIL_PASSWORD = 'wtforms2k16'

# number of times password is hashed
BCRYPT_LOG_ROUNDS = 12


OAUTH_CREDENTIALS = {
    'facebook': {
        'id': '',  # from our official facebook app
        'secret': ''  # from our official facebook app
    },
    'google': {
        'id': '',
        'secret': ''
    }
}
