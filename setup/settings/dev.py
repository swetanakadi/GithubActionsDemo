from .base import *

DEBUG = get_env_variable('DEBUG', 'dev')
SECRET_KEY = os.getenv('SECRET_KEY', 'dev')
ALLOWED_HOSTS.extend(os.getenv('ALLOWED_HOSTS', 'dev'))


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB', 'dev'),
        'USER': os.getenv('POSTGRES_USER', 'dev'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', 'dev'),
        'HOST': os.getenv('POSTGRES_HOST', 'dev'),
        'PORT': os.getenv('POSTGRES_PORT', 'dev')
    }
}

