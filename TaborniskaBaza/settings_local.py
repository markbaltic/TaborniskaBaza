

from TaborniskaBaza.settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sem2017_julijat',
        'USER': 'julijat',
        'PASSWORD': 'v206huao',
        'HOST': 'baza.fmf.uni-lj.si',
        'PORT': '5432',
    }
}