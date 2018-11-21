import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4_3sdgf77&u=#e+7vco%bw-v^bw!c#!si1%$(ax8rs_!$-)w8h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'upload',
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

ROOT_URLCONF = 'django_file_cache.urls'

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

WSGI_APPLICATION = 'django_file_cache.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
# 配置静态文件
STATICFILES_DURS = (os.path.join(BASE_DIR,'static'))
# 访问多媒体文件的路径
MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR,'media')

# 缓存配置
# 小网站低成本
CACHES = {
             # 'default': {
             #     # 指定缓存的类型是文件缓存
             #     'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
             #     # 将缓存的数据保存在该目录下
             #     'LOCATION': 'd:/cache',
             #     'TIMEOUT': 300
             # },
             'default': {
                 # 使用redis做缓存
                 'BACKEND': 'django_redis.cache.RedisCache',
                 # 将缓存的数据保存在该目录下
                 # 缓存的地址
                 'LOCATION': 'redis://112.74.42.138:6379/1',
                 # rediss: //[:password]@localhost:6379 / 0
                 'TIMEOUT': 300,
                 'OPTIONS': {
                     # "PASSWORD": ""
                     # 是否压缩缓存数据
                     "COMPRESSOR": "django_redis.compressors.zlib.ZlibCompressor",
                     # 配置连接池
                     "CONNECTION_POOL_KWARGS": {"max_connections": 100, "retry_on_timeout": True}
                 }
             },

             'session': {
                 # 指定缓存的类型是文件缓存
                 'BACKEND': 'django_redis.cache.RedisCache',
                 # 将缓存的数据保存在该目录下
                 'LOCATION': 'redis://112.74.42.138:6379/15',
                 'TIMEOUT': 300,
                 'OPTIONS': {
                     # "PASSWORD": ""
                     # 是否压缩缓存数据
                     "COMPRESSOR": "django_redis.compressors.zlib.ZlibCompressor",
                     # 配置连接池
                     "CONNECTION_POOL_KWARGS": {"max_connections": 100, "retry_on_timeout": True}
                 }
             },
         },

# session使用redis座位缓存
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "session"