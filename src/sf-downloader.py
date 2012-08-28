'''
Created on Aug 28, 2012

@author: Michal Karm Babacek
'''
import urllib2
import urllib2_kerberos
import properties

opener = urllib2.build_opener()
opener.add_handler(urllib2_kerberos.HTTPKerberosAuthHandler())
resp = opener.open(properties.URL)
print dir(resp), resp.info(), resp.code, resp.read()

