# Though configs are not required in this simple demo,
# any apps except this one will have some sorts of configurations.
# This format of configuration is very extensible.
# The config is used by app.config.from_object(Config) called in __init__.py

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"

    # Configuring SQLite
    # Take defined database path or configure a database named app.db
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "").replace(
        "postgres://", "postgresql://") or \
        "sqlite://" + os.path.join(basedir, "app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Email Configuration
    # for error handling
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['your-email@example.com']

    # Configuring Pagination
    POSTS_PER_PAGE = 20

    # Supported languages (using Babel)
    LANGUAGES = ["en", "es"]
