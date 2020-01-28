#!/usr/bin/env python
import requests, sys
from bs4 import BeautifulSoup as Soup, Tag
     
if __name__ == "__main__":
    if len (sys.argv) != 2 :
            print "Shodan Subdomain Finder by SmoZy\n\nUsage: ./shodan.py [domain] "
            sys.exit (1)

domain = sys.argv[1]
r =requests.get('https://beta.shodan.io/domain/' + domain)
soup = Soup(r.text, 'html.parser')
table = soup.find("table", { "class" : "feature-table u-full-width" })
for row in table.findAll("tr"):
    cells = row.findAll("td")
    if len(cells) == 3:
        entry = cells[0].find(text=True)
        record_type = cells[1].find(text=True)
        value = cells[2].find(text=True)
        if record_type == 'CNAME' and domain in value: 
            delim = value.split('.')
            match = delim[-2] + '.' + delim[-1]
            if match == domain:
                print "{}.{}".format(entry, value)
