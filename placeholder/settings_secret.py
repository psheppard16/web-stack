import os
import sys
import logging
from placeholder.settings import BASE_DIR

# copy to settings_secret.py and generate secret key
SECRET_KEY='JM291MFHAFMA82KFM'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'databases/db.sqlite3'),
        'TEMPLATE_DEBUG': True,
    }
}

DEBUG = True

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
            ],
            'libraries': {
            }
        },
    },
]

if 'test' in sys.argv:
    # disable migration (assumes default is up-to-date in migrations)
    class DisableMigrations(object):
        def __contains__(self, item):
            return True

        def __getitem__(self, item):
            return None


    MIGRATION_MODULES = DisableMigrations()

    # disable debugging and logging because they are slow
    DEBUG = False
    TEMPLATE_DEBUG = False
    logging.disable(logging.CRITICAL)

    # use weakest password hash to improve account creation speed
    PASSWORD_HASHERS = [
        'django.contrib.auth.hashers.MD5PasswordHasher',
    ]
