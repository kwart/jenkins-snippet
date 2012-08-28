'''
Created on Aug 28, 2012

@author: Michal Karm Babacek <mbabacek@redhat.com>
'''

"""
URLs and contexts
"""
BASE_URL = "https://jenkins.mw.lab.eng.bos.redhat.com"
URL = BASE_URL+"/hudson/view/mod_cluster-QE/view/mod_cluster-QE-eap-5x/"
#URL = BASE_URL+"/hudson/view/mod_cluster-QE/view/mod_cluster-QE-eap-6x/"
CONFIG_CONTEXT = "/hudson/job/"
CONFIX_XML = "/config.xml"
REGEXP = ".*<td><a href=\"job\/([^\/]*)\/\">.*"

"""
Target files for storing our jobs
"""
TARGET_FILE = "./xmls/EAP5.xml"
#TARGET_FILE = "./xmls/EAP6.xml"
ENCODING = "utf-8"

"""
Some XML snippets to be added/updated to/in our job configurations.
"""
IRC_PUBLISHER_XML = "\
     <hudson.plugins.ircbot.IrcPublisher>\n\
      <targets>\n\
        <hudson.plugins.im.GroupChatIMMessageTarget>\n\
          <name>#mod_cluster</name>\n\
          <notificationOnly>false</notificationOnly>\n\
        </hudson.plugins.im.GroupChatIMMessageTarget>\n\
      </targets>\n\
      <strategy>ALL</strategy>\n\
      <notifyOnBuildStart>true</notifyOnBuildStart>\n\
      <notifySuspects>false</notifySuspects>\n\
      <notifyCulprits>false</notifyCulprits>\n\
      <notifyFixers>false</notifyFixers>\n\
      <notifyUpstreamCommitters>false</notifyUpstreamCommitters>\n\
      <buildToChatNotifier class=\"hudson.plugins.im.build_notify.SummaryOnlyBuildToChatNotifier\" />\n\
      <matrixMultiplier>ONLY_CONFIGURATIONS</matrixMultiplier>\n\
      <channels />\n\
    </hudson.plugins.ircbot.IrcPublisher>\n"
