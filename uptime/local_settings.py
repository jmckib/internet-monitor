import os


def update_settings(settings):

    settings['DEBUG'] = True
    settings['TEMPLATE_DEBUG'] = True

    settings['DATABASES'] = {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "NAME": "django_deploy",
            "USER": "django",
            "PASSWORD": "dKjLdC",
            "HOST": "localhost",
            "PORT": "5432",
        }
    }
