#!/usr/bin/python2

'''
Created on Aug 28, 2012

@author: Michal Karm Babacek <mbabacek@redhat.com>
'''

import xml.etree.ElementTree as ET
import urllib
import urllib2
import properties
import manipulator as M
import re
import sys
import time
import json

class Processor:
    """
    Processes a raw html page from the Jenkins URL (defined in the properties file).
    """
    jobs = []
    errors = 0

    def getJobs(self):
        opener = urllib2.build_opener()
        opener.addheaders.append(('Cookie', properties.AUTH_COOKIES))
        resp = opener.open(properties.BASE_URL + properties.API_URL)
        jobs_json = json.load(resp)
        self.jobs = [x['name'] for x in jobs_json['jobs']]

    def getJobXML(self, job):
        opener = urllib2.build_opener()
        opener.addheaders.append(('Cookie', properties.AUTH_COOKIES))
        resp = None
        req = properties.BASE_URL + properties.CONFIG_CONTEXT + urllib.quote(job) + properties.CONFIX_XML
        try:
            resp = opener.open(req)
        except urllib2.URLError:
            for trial in range(0, 6):
                sys.stdout.write("...")
                sys.stdout.flush()
                time.sleep(1)
                try:
                    resp = opener.open(req)
                    if resp.code == 200:
                        break
                except urllib2.URLError:
                    sys.stdout.write("...")
        if resp != None and resp.code == 200:
            return resp.read()
        else:
            return None

if __name__ == '__main__':
    if len(sys.argv) > 1:
        mask = sys.argv[1]
    else:
        mask = '^.*$'
    regex_job_name = re.compile(mask)
    target_file = open(properties.TARGET_FILE, 'w')
    agregated_root = ET.Element('rootview')
    processor = Processor()
    manipulator = M.Manipulator()
    processor.getJobs()
    #Testing...
    #processor.jobs = ['eap-5x-mod_cluster-python-editor','eap-5x-mod_cluster-python-editor-clone']
    #print processor.jobs
    number_of_jobs = len(processor.jobs)
    number_of_jobs_done = 0.
    for job in processor.jobs:
        number_of_jobs_done += 1
        progress = number_of_jobs_done / (float(number_of_jobs) / 100.)
        sys.stdout.write("Progress: %d %%, Processing job %s ..." % (progress, job))
        sys.stdout.flush()
        if regex_job_name.match(job):
            xml = processor.getJobXML(job)
            if xml == None:
                sys.stdout.write(" ERROR\n")
                processor.errors += 1
            else:
                job_xml_root = ET.fromstring(xml)
                job_name = ET.Element('view')
                job_name.set('name', job)
                job_name.append(job_xml_root)
                agregated_root.append(manipulator.manipulate(job_name))
                sys.stdout.write(" DONE\n")
        else:
            sys.stdout.write(" SKIPPED\n")
    ET.ElementTree(agregated_root).write(target_file, encoding = properties.ENCODING, xml_declaration = True)
    target_file.close()
    if processor.errors == 0:
        print "%d jobs processed. All the xml configurations are in %s file." % (number_of_jobs, properties.TARGET_FILE)
    else:
        print "%d jobs processed. Some of the xml configurations are in %s file. There were %d errors." % (number_of_jobs, properties.TARGET_FILE, processor.errors)
