#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests


response = requests.get("https://access.redhat.com/errata/RHSA-2021:2314")
page = response.text


soup = BeautifulSoup(page, "html.parser")
cve_tag = soup.find(id="cves" )
cve_list=list(cve_tag.getText().split('\n'))
while("" in cve_list) :
    cve_list.remove("")

for i in range(1,len(cve_list)):
    print ("https://access.redhat.com/security/cve/%s" %cve_list[i])
