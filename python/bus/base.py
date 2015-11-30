import os, sys
lib_path = os.path.abspath(os.path.join('..', '..', '..', 'lib'))
sys.path.append(lib_path)
from Data.data import *

travels = generateTravels()
links = generateLiaisons()

for l in links:
	print l

