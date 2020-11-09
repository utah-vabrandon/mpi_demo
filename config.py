# config.py

from decouple import config

import logging


DEBUG = config('DEBUG', default=True)
logfile = config('LOGFILE', default=None)

DATABASES = {
    'default': config(
        'DATABASE_URI',
        default='sqlite:///test.sqlite3'
    )
}

IDVIEWTYPE = config('IDVIEWTYPE', default='full')
CLASSIFIER = config('CLASSIFIER', default='logistic')

if DEBUG:
    loglevel = 'DEBUG'
else:
    loglevel = 'INFO'


def log_setup(loglevel, logfile):
    if loglevel == 'DEBUG':
        level = logging.DEBUG
    else:
        level = logging.INFO
    
    logging.basicConfig(
        format='[%(asctime)s] %(levelname)s: %(message)s',
        filename=logfile, 
        level=level)

log_setup(loglevel, logfile)
            


    

