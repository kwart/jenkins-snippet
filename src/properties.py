'''
Created on Aug 28, 2012

@author: Michal Karm Babacek <mbabacek@redhat.com>
'''

"""
URLs and contexts
"""
BASE_URL = "https://jenkins.mw.lab.eng.bos.redhat.com"
#URL = BASE_URL+"/hudson/view/mod_cluster/view/mod_cluster-QE/view/mod_cluster-QE-eap-5x/"
URL = BASE_URL+"/hudson/view/mod_cluster/view/mod_cluster-QE/view/mod_cluster-QE-eap-6x/"
CONFIG_CONTEXT = "/hudson/job/"
CONFIX_XML = "/config.xml"
API_URL="/api/json"

"""
Target files for storing our jobs
"""
#TARGET_FILE = "./xmls/EAP5.xml"
TARGET_FILE = "./xmls/EAP6.xml"
ENCODING = "utf-8"
LEAVE_UNCHANGED = True

"""
Some XML snippets to be added/updated to/in our job configurations.
"""
IRC_PUBLISHER_XML = """
     <hudson.plugins.ircbot.IrcPublisher>
      <targets>
        <hudson.plugins.im.GroupChatIMMessageTarget>
          <name>#mod_cluster</name>
          <notificationOnly>false</notificationOnly>
        </hudson.plugins.im.GroupChatIMMessageTarget>
      </targets>
      <strategy>ALL</strategy>
      <notifyOnBuildStart>true</notifyOnBuildStart>
      <notifySuspects>false</notifySuspects>
      <notifyCulprits>false</notifyCulprits>
      <notifyFixers>false</notifyFixers>
      <notifyUpstreamCommitters>false</notifyUpstreamCommitters>
      <buildToChatNotifier class=\"hudson.plugins.im.build_notify.SummaryOnlyBuildToChatNotifier\" />
      <matrixMultiplier>ONLY_CONFIGURATIONS</matrixMultiplier>
      <channels />
    </hudson.plugins.ircbot.IrcPublisher>
"""
