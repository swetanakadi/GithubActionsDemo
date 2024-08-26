from .base import *

DEBUG = get_env_variable('DEBUG', 'prod')
print('DEBUG', DEBUG)
SECRET_KEY = get_env_variable('SECRET_KEY', 'prod')
hosts = get_env_variable('ALLOWED_HOSTS', 'prod').split(',')
for host in hosts:
    if host:
        ALLOWED_HOSTS.append(host.strip())


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB', 'prod'),
        'USER': os.getenv('POSTGRES_USER', 'prod'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', 'prod'),
        'HOST': os.getenv('POSTGRES_HOST', 'prod'),
        'PORT': os.getenv('POSTGRES_PORT', 5432)
    }
}