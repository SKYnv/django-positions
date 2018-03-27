SECRET_KEY = 'you_saw_nothing.'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

INSTALLED_APPS = [
    'django_positions_2.apps.DjangoPositions2Config',
    'tests'
]
