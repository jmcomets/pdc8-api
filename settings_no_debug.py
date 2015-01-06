from settings import *
import dj_database_url

DEBUG = False
TEMPLATE_DEBUG = False

# Secret key from $SECRET_KEY
SECRET_KEY = os.environ.get('SECRET_KEY')

# Parse database configuration from $DATABASE_URL
DATABASES['default'] =  dj_database_url.config()
