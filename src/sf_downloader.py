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
import sys

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
    target_file = open(properties.TARGET_FILE, 'w')
    agregated_root = ET.Element('rootview')
    processor = Processor()
    processor.getJobs()
    #processor.jobs = ['eap-6x-mod_cluster-benchmark-mod_cluster-clusterlab', 'eap-6x-mod_cluster-benchmark-mod_cluster-mix-version']
    print processor.jobs
    number_of_jobs = len(processor.jobs)
    number_of_jobs_done = 0.
    for job in processor.jobs:
        progress = number_of_jobs_done / (float(number_of_jobs) / 100.)
        message = "Progress: %d %%, Processing job %s ..." % (progress, job)
        sys.stdout.write(message)
        xml = processor.getJobXML(job)
        job_xml_root = ET.fromstring(xml)
        job_name = ET.Element(processor.jobs[0])
        job_name.append(job_xml_root)
        agregated_root.append(job_name)
        print " DONE"
        number_of_jobs_done += 1
    ET.ElementTree(agregated_root).write(target_file)
    target_file.close()
    print "Processing %d jobs took %f seconds. All the xml configurations are in %s file." % (number_of_jobs, (time.clock() - start), properties.TARGET_FILE)

