"""
Django settings for saashome project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
from decouple import config
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("DJANGO_SECRET_KEY")


# Email Config
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config("EMAIL_HOST" , cast=str , default= "smtp.gmail.com")
EMAIL_PORT = config("EMAIL_PORT" , cast=str , default="587")
EMAIL_USE_TLS = config("Email_USE_TLS" , cast=bool , default = True)
EMAIL_USE_SSL = config("EMAIL_USE_SSL", cast= bool , default = False)
EMAIL_HOST_USER = config("EMAIL_HOST_USER" , cast= str , default = None)
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD" , cast=str , default=None)


ADMIN_USER_NAME = config("ADNIN_USER_NAME" , default = "Admin user")
ADMIN_USER_EMAIL = config("ADMIN_USER_EMAIL" , default = None)

MANAGERS=[]
ADMINS=[]

if all([ADMIN_USER_NAME, ADMIN_USER_EMAIL]):
    ADMINS += [
        (f'{ADMIN_USER_NAME}', f'{ADMIN_USER_EMAIL}')
    ]
    MANAGERS=ADMINS


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DJANGO_DEBUG", cast=bool)

print("DEBUG", DEBUG, type(DEBUG))

ALLOWED_HOSTS = [
    ".railway.app", 
]
if DEBUG:
    ALLOWED_HOSTS +=[
        "localhost",
        "127.0.0.1",
    ]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    #my-apps
    "visits",
    "commando",
    "auths",

    #third-party-apps
    "allauth_ui",
    'allauth',
    'allauth.account',
    "widget_tweaks",
    "slippers",
    
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    "allauth.account.middleware.AccountMiddleware",
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
       
]

ROOT_URLCONF = 'saashome.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/ "templates"],
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

WSGI_APPLICATION = 'saashome.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

CONN_MAX_AGE = config("CONN_MAX_AGE", cast= int, default= 30)
DATABASE_URL = config("DATABASE_URL" ,cast = str)


if DATABASE_URL is not None:
    import dj_database_url
    DATABASES = {
        "default" : dj_database_url.config(
            default = DATABASE_URL,
            conn_max_age = CONN_MAX_AGE ,
            conn_health_checks = True
        )
    }
    


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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

# Django aalauth Config
LOGIN_REDIRECT_URL = "/"
ACCOUNT_AUTHENTICATION_METHOD = "username_email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_EMAIL_SUBJECT_PREFIX = "[CFE]"
AUTHENTICATION_BACKENDS = [
    
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',
    
]

SOCIALACCOUNT_PROVIDERS = {
}


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_BASE_DIRS = BASE_DIR / "staticfiles"
STATICFILES_VENDOR_DIRS = STATICFILES_BASE_DIRS / "vendors"

#source for python manage.py collectstatic

STATICFILES_DIRS = [
    STATICFILES_BASE_DIRS  
]


#output for python manage.py collectstatic
#local-cdn

STATIC_ROOT = BASE_DIR / "local-cdn"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# import os

# if DEBUG: 
#     STATICFILES_DIRS = [os.path.join(BASE_DIR, "templates")]
    
# else:
#     STATIC_ROOT = [os.path.join(BASE_DIR, "templates")]
    
# MEDIA_ROOT = [os.path.join(BASE_DIR, "templates")]


