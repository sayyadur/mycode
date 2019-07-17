#!/usr/bin/env python3
import urllib.request, re
def get_external_ip():
    url = 'http://checkip.dyndns.org'
    requesty = urllib.request.urlopen(url).read().decode('utf-8')
    externalIP = re.findall('\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}', requesty)
    return externalIP

print('Your public IP address is: ' + str(get_external_ip()) )

