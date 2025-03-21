import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'your-secret-key-here'  # Replace with your own secret key

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False  # Change to False in production

ALLOWED_HOSTS = ['*']  # Adjust this based on your deployment needs

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Your apps
    'bookshelf',
    'users',
    'relationship_app',
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

# ✅ Fix project name (match folder structure)
ROOT_URLCONF = 'libraryproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

# ✅ Fix project name in WSGI
WSGI_APPLICATION = 'libraryproject.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static & Media Files
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ✅ Custom User Model (Corrected)
AUTH_USER_MODEL = "bookshelf.CustomUser"

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ✅ Security settings
SECURE_BROWSER_XSS_FILTER = True  # Prevents XSS attacks
X_FRAME_OPTIONS = "DENY"  # Prevents clickjacking
SECURE_CONTENT_TYPE_NOSNIFF = True  # Prevents MIME sniffing
CSRF_COOKIE_SECURE = True  # Ensures CSRF tokens are only sent over HTTPS
SESSION_COOKIE_SECURE = True  # Ensures session cookies are only sent over HTTPS
SECURE_SSL_REDIRECT = True  # Redirects all non-HTTPS requests to HTTPS
SECURE_HSTS_SECONDS = 31536000  # Enforces HTTPS for one year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Includes all subdomains in HSTS policy
SECURE_HSTS_PRELOAD = True  # Allows HSTS preloading
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')  # Ensures Django detects HTTPS correctly behind a proxy
