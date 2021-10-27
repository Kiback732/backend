import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEVELOPMENT = True
    DEBUG = True

    SECRET_KEY = os.environ.get('SECRET_KEY') or '123456789'
    SQLALCHEMY_DATABASE_URI = os.environ.get('POSTGRESQL_URL') or 'postgresql://worker:worker@localhost/app'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER') or os.path.join(basedir, 'upload')
    ALLOWED_IMAGE_EXTENSIONS = ['JPEG', 'JPG', 'PNG', 'GIF']
