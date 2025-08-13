import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = '2abbb66e6262d8a471b69c7jayedhossainjibona03a0c74bjibon969'
DEBUG = True
ALLOWED_HOSTS = ['*']
BASE_URL = "*"


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'smart_mailer_db',
#         'USER': 'dbadmin',
#         'PASSWORD': 'smart75#@!Mailer',
#         'HOST': '127.0.0.1',
#         'PORT': '5432',
#     }
# }


try:
    # Sending E-mail Configuration ==============================
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_HOST_USER = 'jibon.belasea@gmail.com'
    EMAIL_HOST_PASSWORD = 'rcqtdxesqufgebtx'  # Use app password
except:
    pass


