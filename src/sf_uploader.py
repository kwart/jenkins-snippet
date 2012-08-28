#!/usr/bin/python

'''
Created on Aug 28, 2012

@author: Michal Karm Babacek <mbabacek@redhat.com>
'''
import xml.etree.ElementTree as ET
import urllib2
import urllib2_kerberos
import properties
import sys

class Processor:
    """
    Meh...
    """
    job_elements = []

    def getJobs(self):
        tree = ET.parse(properties.TARGET_FILE)
        root = tree.getroot()
        self.job_elements = list(root)

if __name__ == '__main__':
    processor = Processor()
    processor.getJobs()
    for job in processor.job_elements:
        project = job.find("project")
        project = ET.tostring(project, encoding=properties.ENCODING)
        opener = urllib2.build_opener()
        opener.add_handler(urllib2_kerberos.HTTPKerberosAuthHandler())
        req = urllib2.Request(properties.BASE_URL + properties.CONFIG_CONTEXT + job.tag + properties.CONFIX_XML, data = project, headers = { "Content-type" : "text/xml; charset="+properties.ENCODING})
        response = opener.open(req)
        print response.code

