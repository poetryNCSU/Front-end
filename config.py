from os import path

# App details
BASE_DIRECTORY = path.abspath(path.dirname(__file__))
DEBUG = True
SECRET_KEY = '8a3b3879dd6b8330543bee2e43a3390e'

# Database details
SQLALCHEMY_DATABASE_URI = '{0}{1}'.format('sqlite:///',
                                          path.join(BASE_DIRECTORY, 'app.db'))
