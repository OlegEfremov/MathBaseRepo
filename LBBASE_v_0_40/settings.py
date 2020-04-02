import os.path

from LBBASE_v_0_40.someutils import get_env_variable

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_env_variable('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = get_env_variable('DEBUG')

ALLOWED_HOSTS = [get_env_variable('ALLOWED_HOSTS')]



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'django.contrib.sites',
    'mptt',
    'django_mptt_admin',
    'import_export',
    'apps.Main.apps.MainConfig',
    'apps.Solution_Catalog.apps.SolutionCatalogConfig',
    'apps.Edit_MathAttribute_Catalog.apps.EditMathattributeCatalogConfig',
    'apps.Full_Search.apps.FullSearchConfig',
    'apps.Edit_Task.apps.EditTaskConfig',
    'apps.Edit_Solution.apps.EditSolutionConfig',
    'apps.Table_Of_Tasks.apps.TableOfTasksConfig',
    'apps.Edit_Source_Catalog.apps.EditSourceCatalogConfig',
    'apps.Export.apps.ExportConfig',
    'apps.BelovedCat.apps.BelovedcatConfig',
    'apps.Test_Generated.apps.TestGeneratedConfig',
    'apps.All_Search.apps.AllSearchConfig',
    'registration'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'LBBASE_v_0_40.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'LBBASE_v_0_40.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'lbbase_db',
        # 'OPTIONS': {
        #     'init_command': 'SET innodb_strict_mode=1',
        # },
        'USER': get_env_variable('MYSQL_USER'),
        'PASSWORD': get_env_variable('MYSQL_DB_PASSWORD'),
        # 'HOST': '127.0.0.1',
        # 'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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

REGISTRATION_SALT = 'customregistrationsalt'        # If True, users can register
REGISTRATION_OPEN = True        # If True, users can register
ACCOUNT_ACTIVATION_DAYS = 7     # One-week activation window; you may, of course, use a different value.
REGISTRATION_AUTO_LOGIN = True  # If True, the user will be automatically logged in.
LOGIN_REDIRECT_URL = '/main/main_page'  # The page you want users to arrive at after they successful log in
LOGIN_URL = '/accounts/login/'  # The page users are directed to if they are not logged in,
                                # and are trying to access pages requiring authentication

# REGISTRATION_FORM = 'registration.forms.RegistrationFormUniqueEmail'

# AUTH_USER_EMAIL_UNIQUE = True

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'labreslav239@gmail.com'
EMAIL_HOST_PASSWORD = 'amtro915kvadri'
EMAIL_PORT = 587
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'



# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

ADMIN = [('Leo', 'leobreslav@gmail.com')]

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

MEDIA_URL='/media/'

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

STATICFILES_DIRS = [os.path.join('static'), ]

LOGIN_REDIRECT_URL = '/'

# SITE_ID = 1


# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'file': {
#             'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
#             'class': 'logging.FileHandler',
#             'filename': '/home/leobreslav/logs/django.log',
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['file'],
#             'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
#             'propagate': True,
#         },
#     },
# }

