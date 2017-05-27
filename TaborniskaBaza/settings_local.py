

from TaborniskaBaza.settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'TBaza',
        'USER': 'tabornik',
        'PASSWORD': 'tabornik',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}