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
import re


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
    script, mask = sys.argv
    regex_job_name = re.compile(mask)
    processor = Processor()
    processor.getJobs()
    number_of_jobs = len(processor.job_elements)
    number_of_jobs_done = 0.
    for job in processor.job_elements:
        number_of_jobs_done += 1
        progress = number_of_jobs_done / (float(number_of_jobs) / 100.)
        sys.stdout.write("Progress: %d %%, Processing job %s ..." % (progress, job.tag))
        sys.stdout.flush()
        project = job.find("project")
        if project == None:
            # it can be also a matrix job, lets try it
            project = job.find("matrix-project")
        project = ET.tostring(project, encoding=properties.ENCODING)
        if regex_job_name.match(job.tag):
            opener = urllib2.build_opener()
            opener.add_handler(urllib2_kerberos.HTTPKerberosAuthHandler())
            req = urllib2.Request(properties.BASE_URL + properties.CONFIG_CONTEXT + job.tag + properties.CONFIX_XML, data = project, headers = { "Content-type" : "text/xml; charset="+properties.ENCODING})
            response = opener.open(req)
            if response.code == 200:
                sys.stdout.write(" DONE\n")
            else:
                sys.stdout.write(" ERROR code: %d\n" % response.code)
        else:
            sys.stdout.write("SKIPPED\n")
        sys.stdout.flush()
    print "\n%d jobs processed. All the xml configurations were uploaded from file %s to your Jenkins :-)" % (number_of_jobs, properties.TARGET_FILE)

