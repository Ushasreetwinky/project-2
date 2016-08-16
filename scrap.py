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



soup=make_soup("https://learn.gramener.com/codogram/#people/?q=DRL-Scorecard")
for record in soup.findAll("div", attrs={"id": "people"}):
	playerdata = ""
	for data in record.findAll('span',attrs={"class":"people-name"}):
		playerdata = playerdata + ',' + data.text

print "data: ",playerdata


page = requests.get('https://learn.gramener.com/codogram/#people/?q=DRL-Scorecard')
tree = html.fromstring(page.content)
#This will create a list of buyers:
buyers = tree.xpath('//div[@id="people"]/text()')
#This will create a list of prices
prices = tree.xpath('//span[@class="people-name"]/text()')
print "buyers: ",buyers
print prices