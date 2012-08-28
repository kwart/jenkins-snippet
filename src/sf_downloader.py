#!/usr/bin/python

'''
Created on Aug 28, 2012

@author: Michal Karm Babacek <mbabacek@redhat.com>
'''
import xml.etree.ElementTree as ET
import urllib2
import urllib2_kerberos
import properties
import re
import time

class Processor:
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
                
    def getJobXML(self, job):
        opener = urllib2.build_opener()
        opener.add_handler(urllib2_kerberos.HTTPKerberosAuthHandler())
        resp = opener.open(properties.BASE_URL+properties.CONFIG_CONTEXT+job+properties.CONFIX_XML)
        return resp.read()

if __name__ == '__main__':
    start = time.clock()
    targetFile = open(properties.TARGET_FILE, 'w')
    agregatedRoot = ET.Element('rootview')
    processor = Processor()
    processor.getJobs()
    processor.jobs = ['eap-6x-mod_cluster-benchmark-mod_cluster-clusterlab', 'eap-6x-mod_cluster-benchmark-mod_cluster-mix-version']
    print processor.jobs
    for job in processor.jobs:
        print 'Processing job %s ...' % job
        xml = processor.getJobXML(job)
        '''
        Meh, no XML processing will be necessary, we just save it...
        root = ET.fromstring(xml)
        for child in root:
            if child.tag == "description":
                print child.tag, child.attrib, child.text
        '''
        jobXMLroot = ET.fromstring(xml)
        jobName = ET.Element(processor.jobs[0])
        jobName.append(jobXMLroot)
        agregatedRoot.append(jobName)
        print 'DONE\n'
    ET.ElementTree(agregatedRoot).write(targetFile)
    targetFile.close()
    print "Processing %d jobs took %f seconds. All the xml configurations are in %s file." % (len(processor.jobs), (time.clock() - start), properties.TARGET_FILE)
