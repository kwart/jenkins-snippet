'''
Created on Aug 28, 2012

@author: Michal Karm Babacek <mbabacek@redhat.com>
'''
BASE_URL = "https://jenkins.mw.lab.eng.bos.redhat.com"
#URL = "https://jenkins.mw.lab.eng.bos.redhat.com/hudson/view/mod_cluster-QE/view/mod_cluster-QE-eap-5x/"
URL = BASE_URL+"/hudson/view/mod_cluster-QE/view/mod_cluster-QE-eap-6x/"
CONFIG_CONTEXT = "/hudson/job/"
CONFIX_XML = "/config.xml"
REGEXP = ".*<td><a href=\"job\/([^\/]*)\/.*"
TARGET_FILE = "./test.xml"