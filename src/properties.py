'''
Created on Aug 28, 2012

@author: Michal Karm Babacek <mbabacek@redhat.com>
'''

"""
URLs and contexts
"""
BASE_URL = "http://jenkins.hazelcast.com"
#URL = BASE_URL+"/hudson/view/mod_cluster/view/mod_cluster-QE/view/mod_cluster-QE-eap-5x/"
URL = BASE_URL+"/"
CONFIG_CONTEXT = "/job/"
CONFIX_XML = "/config.xml"
API_URL="/api/json"

# copy cookies from your browser - e.g. in Chrome (https://stackoverflow.com/a/21919431/653069):
# Hit F12 to open the developer console and switch to the Network tab.
# Reload Jenkins page
# Right click the relevant request, and select "Copy request headers" and in a text editor just pick the "Cookie:" value
AUTH_COOKIES='_ga=...;... JSESSIONID...=...'

"""
Target files for storing our jobs
"""
TARGET_FILE = "jenkins-hazelcast.xml"
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
