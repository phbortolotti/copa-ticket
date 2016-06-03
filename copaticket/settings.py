from os import environ


DEBUG = environ.get('DEBUG', False)
SECRET_KEY = environ.get('SECRET_KEY')
CARTOLAFC_EMAIL = environ.get('CARTOLAFC_EMAIL')
CARTOLAFC_PASSWORD = environ.get('CARTOLAFC_PASSWORD')
CARTOLAFC_SID = 438
CARTOLAFC_LIGA = 'copa-ticket'
