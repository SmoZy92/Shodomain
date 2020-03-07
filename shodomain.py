#!/usr/bin/env python3
import requests, sys, json

def tldSorting(subdomainList):
    localsortedlist = list()
    finallist = list()
    for item in subdomainList:
        Reverseddomain = ".".join(str(item).split('.')[::-1])
        localsortedlist.append(Reverseddomain)

    sortedlist = sorted(localsortedlist)

    for item in sortedlist:
        reReverseddomain = ".".join(str(item).split('.')[::-1])
        finallist.append(reReverseddomain)

    return finallist

if __name__ == "__main__":
    if len (sys.argv) != 3 :
            print("Shodan Subdomain Finder by SmoZy\n\nUsage: ./shodan.py [API Key] [Domain]")
            sys.exit (1)

apikey = sys.argv[1]
domain = sys.argv[2]

r =requests.get('https://api.shodan.io/dns/domain/' + domain + '?key=' + apikey)
data = json.loads(r.text)
subdomains = set()
for item in data["data"]:
    entry = item["subdomain"]  
    record_type = item["type"]
    value = item["value"]
    if record_type == 'CNAME' and domain in value: 
        delim = value.split('.')
        match = delim[-2] + '.' + delim[-1]
        if match == domain:
            subdomains.add(value)

for s in tldSorting(subdomains): 
    print(s)
    
