import requests
import re
from bs4 import BeautifulSoup
import datetime
import random


#get internal link
def getInternalLink(soup, includeUrl):
    internalLinks = []
    for link in soup.find_all("a", href = re.compile("^(/|.*'+includeUrl+')")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                internalLinks.append(link.attrs['href'])
    return internalLinks

# get external link
def getExternalLink(soup, excludeUrl):
    externalLinks = []
    for link in soup.find_all("a", href = re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks

def splitAddress(address):
    addressParts = address.replace("http://", "").split("/")
    return addressParts

# def parseExternalLink(startingPage):
#     wb_data = requests.get(startingPage)
#     soup = BeautifulSoup(wb_data, 'lxml')
#     externalLinks = getExternalLink(soup, splitAddress(startingPage)[0])
#     if len(externalLinks) == 0:
#         internalLinks = getInternalLink(soup, startingPage)

def getRandomExternalLink(startingPage):
    wb_data = requests.get(startingPage)
    soup = BeautifulSoup(wb_data.text)
    externalLinks = getExternalLink(soup, splitAddress(startingPage)[0])
    if len(externalLinks) == 0:
        internalLinks = getInternalLink(soup, startingPage)
        return getExternalLink(internalLinks[random.randint(0, len(internalLinks) - 1)])
    else:
        return externalLinks[random.randint(0, len(externalLinks) - 1)]
def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink(startingSite)
    print("Random link is: " + externalLink)
    followExternalOnly(externalLink)


followExternalOnly('http://oreilly.com')

