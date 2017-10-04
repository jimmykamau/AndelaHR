import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.environ['SECRET_KEY']


class ProductionConfig(object):
    DEBUG = False


class StagingConfig(object):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(object):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(object):
    TESTING = True
