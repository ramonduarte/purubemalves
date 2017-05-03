# coding=utf-8
"""
Django settings for tansparency project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import dj_database_url
from local_settings import *
import dropbox


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Application definition
INSTALLED_APPS = (
    # 'admin_tools',
    # 'admin_tools.theming',
    # 'admin_tools.menu',
    # 'admin_tools.dashboard',

    # django-autocomplete-light (2017/03/29)
    'dal',
    'dal_select2',

    # Social OAuth logins (2017/03/10)
    'social_django',

    # Forms usability improvements (2017/03/10)  TODO: fix this date (2017/03/15)
    'widget_tweaks',

    # CPF and CEP form fields (2017/03/10)  TODO: fix this date (2017/03/15)
    'localflavor',

    # Main app, handles internal management (2017/03/10)  TODO: fix this date (2017/03/15)
    'website',

    # Website at https://purubemalves.com.br (2017/03/10)  TODO: fix this date (2017/03/15)
    'home',

    # Applications for students performance tracking (2017/03/10)  TODO: fix this date (2017/03/15)
    'projeto_redacao',
    'controle_de_frequencia',

    # Feedback meta applications (2017/03/10)  TODO: fix this date (2017/03/15)
    'issues',
    'issues.templatetags',

    # Affirmative actions management (2017/03/10)
    'politicas_afirmativas',

    # Students views  (2017/03/15)
    'alunos',

    # Reports views  (2017/03/21)
    'reports',

    # Static content distribution (2017/03/10)
    'storages',


    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    # 'sslify.middleware.SSLifyMiddleware',  # TODO: Decomment this line before pushing (2017/03/14)
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',

    # Social OAuth login handler
    'social_django.middleware.SocialAuthExceptionMiddleware',
)

ROOT_URLCONF = 'transparency.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_ROOT, '../static/templates/'),
            os.path.join(BASE_DIR, '/static/templates/'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            # 'loaders': [
            #     'admin_tools.template_loaders.Loader',
            # ],
            'libraries': {
                # Templete tools for dictionaries (2017/03/15)
                'dict_filters': 'issues.templatetags.dict_filters',
            },
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # Social OAuth login context processors
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

# Social & Internal logins (2017/03/10)
AUTHENTICATION_BACKENDS = (
    # 'social_core.backends.github.GithubOAuth2',
    # 'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.facebook.FacebookOAuth2',

    'django.contrib.auth.backends.ModelBackend',
)

# Login information for the Alunos application (2017/03/15)
LOGIN_URL = 'login'
LOGOUT_URL = 'alunos/logout'
LOGIN_REDIRECT_URL = '/alunos'


# Django's main web application address
WSGI_APPLICATION = 'transparency.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'pt-BR'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Update database configuration with $DATABASE_URL.
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
ENCRYPT_URL = '/.well-known/'
# noinspection PyUnresolvedReferences
ENCRYPT_ROOT = os.path.join(STATIC_ROOT, '.well-known')

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, '../static'),
)

# STATICFILES_FINDERS = (
#     'django.contrib.staticfiles.finders.AppDirectoriesFinder',
# )

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

# Dropbox storage settings (2017/03/15)
dbx = dropbox.Dropbox(DROPBOX_OAUTH2_TOKEN)

SECURE_SSL_REDIRECT = False
ADMIN_SITE_HEADER = "Pré-Universitário Comunitário Rubem Alves"
ADMIN_INDEX_TITLE = "Administração do Projeto"
