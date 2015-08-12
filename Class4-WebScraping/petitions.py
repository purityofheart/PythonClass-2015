from bs4 import BeautifulSoup
import urllib2
import csv 

web_address='https://petitions.whitehouse.gov/petitions'
web_page = urllib2.urlopen(web_address)
soup = BeautifulSoup(web_page.read())

next_href=soup.find_all('a',{"class":"clear show-more-petitions-bar no-follow"})[0]['href']
next_page = urllib2.urlopen('https://petitions.whitehouse.gov/'+next_href)
next_soup = BeautifulSoup(next_page.read())

soup=next_soup

#Repeat


