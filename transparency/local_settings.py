# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/
DEBUG = True
ALLOWED_HOSTS = [
    '138.197.114.82',
    'localhost',
    '127.0.0.1',
    'purubemalves.com.br',
    'www.purubemalves.com.br',
    'pura-admin.herokuapp.com',
    'www.pura-admin.herokuapp.com',
]

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qdw#44*1ohief*q_^4tl3x_ptwtgmrx@f#td(93c%3x5(d46+q'

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'transparency',
        'USER': 'ramonmelo',
        'PASSWORD': '4iquesaco',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# GitHub personal data
GITHUB_USER = 'ramonduarte'
GITHUB_PASSWORD = '4iquesaco'
GITHUB_REPOSITORY = 'purubemalves'
GITHUB_LOCALFILE = 'github.txt'

# Dropbox storage data
DROPBOX_OAUTH2_TOKEN = 'LcfFCBAyqmAAAAAAAAAACCro2kD-nhH0LIGYiVGdz1x1a7AoWOb2SeJIc26Rrg7r'
DROPBOX_ROOT_PATH = ''

# Facebook Social OAuth data
SOCIAL_AUTH_FACEBOOK_KEY = '1715254145386736'  # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = 'e89f6259b74bd56f2134ab838f11fc8a'  # App Secret
