#!/var/www/itsp_tcb/venv/bin/python3
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/var/www/itsp_tcb/')

from backend import app as application
