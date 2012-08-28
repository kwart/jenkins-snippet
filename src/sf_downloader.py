#!/usr/bin/python

'''
Created on Aug 28, 2012

@author: Michal Karm Babacek
'''
import urllib2
import urllib2_kerberos
import properties
import re


class PageProcessor:
    """
    Processes a raw html page from the Jenkins URL (defined in the properties file).
    """
    jobs = []

    def getJobs(self):
        opener = urllib2.build_opener()
        opener.add_handler(urllib2_kerberos.HTTPKerberosAuthHandler())
        resp = opener.open(properties.URL)
        regex = re.compile(properties.REGEXP)
        for line in resp.read().split('\n'):
            result = regex.search(line)
            if result != None:
                self.jobs.append(result.groups()[0])

if __name__ == '__main__':
    pp = PageProcessor()
    pp.getJobs()
    print pp.jobs
    

