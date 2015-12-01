import os, sys
lib_path = os.path.abspath(os.path.join('..', '..', '..', 'lib'))
sys.path.append(lib_path)
from Data.data import *

links = generateLiaisons()
travels = generateTravels(links)	

#show travels
#for t in travels:
#	print t.toString()

#show links
#print links
#get a links
#print 'Link : ' + str('T22' + ':' + 'T23') +' >>>  time:  ' + links.get('T22:T23').time + '   dist: ' + links.get('T22:T23').dist


for tu in travels[0].travelUncompatible:
	print tu.toString()
