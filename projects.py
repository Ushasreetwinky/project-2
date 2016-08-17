from bs4 import BeautifulSoup

import urllib2
from urllib2 import urlopen 
import os
from bs4 import BeautifulSoup
import requests
import base64
import sys

def make_soup(url):
	print sys.argv
	base64string = base64.encodestring('%s:%s' % ("ushasree.ginne@gramener.com", "Ananya28")).replace('\n', '')
	request = urllib2.Request(url)
	request.add_header("Authorization", "Basic %s" % base64string) 
	result = urllib2.urlopen(request)
	soupdata = BeautifulSoup(result, "html.parser")
	return soupdata



soup=make_soup("https://learn.gramener.com/codogram/#projects/")
print soup
for record in soup.findAll("div", attrs={"class": "table-responsive"}):
	playerdata = ""
	for data in record.findAll('tr'):
		playerdata = playerdata + ',' + data.text
		print playerdata

