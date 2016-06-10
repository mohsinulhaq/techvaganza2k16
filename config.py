DEBUG = True
SECRET_KEY = 'FsdfswsskfhAOCABSKJFNAKdfbgfgaJCNWOACNQWIKXNxbcqcnskjcnIUH287R2YRHI2132FVJBKVBJSVB'
SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/tv_db'
SQLALCHEMY_TRACK_MODIFICATIONS = True  # Just to suppress warnings.

# For flask
UPLOAD_FOLDER = '/tmp'
ALLOWED_EXTENSIONS= set(['txt', 'pdf', 'doc', 'docx'])

# For flask debug toolbar.
DEBUG_TB_INTERCEPT_REDIRECTS = False
