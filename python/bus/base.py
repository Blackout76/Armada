import os, sys
lib_path = os.path.abspath(os.path.join('..', '..', '..', 'lib'))
sys.path.append(lib_path)
from Data.data import *

links = generateLiaisons()
travels = generateTravels(links)	

#show travels
for t in travels:
	print t.toString()

#show links
for l in links:
	print l.get('linkName') + ' ' + l.get('link').toString()

