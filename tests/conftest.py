import sys
import os

APP_PATH = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))
if APP_PATH not in sys.path:
        sys.path.insert(0, APP_PATH)
