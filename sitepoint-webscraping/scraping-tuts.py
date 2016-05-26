from urllib import urlopen

# Sending the http request
webpage = urlopen('http://dada.theblogbowl.in/').read()

from bs4 import BeautifulSoup
# making the soup! yummy :)
soup = BeautifulSoup(webpage, 'html5lib')