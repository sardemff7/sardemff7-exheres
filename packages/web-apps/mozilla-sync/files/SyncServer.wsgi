import os
import sys
import site
from logging.config import fileConfig
from ConfigParser import NoSectionError

ini_file = os.path.join('/etc/mozilla-sync/SyncServer.ini')
try:
    fileConfig(ini_file)
except NoSectionError:
    pass

from paste.deploy import loadapp
application = loadapp('config:%s'% ini_file)
