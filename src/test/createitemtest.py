import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from mainfile.createitem import createitem

check = createitem()
check.create("item")