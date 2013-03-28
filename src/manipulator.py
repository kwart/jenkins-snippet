#!/usr/bin/python

'''
Created on Aug 28, 2012

@author: Michal Karm Babacek <mbabacek@redhat.com>
'''
import xml.etree.ElementTree as ET
import properties

class Manipulator:
    """
    Meh...
    """
    def manipulate(self, element):
        """
        Before we save the file, we may want to add or remove some
        elements as well as edit some text.
        """
        if not properties.LEAVE_UNCHANGED:
            element = self.addIRCNotification(element)
            element = self.removeObsoleteShellTask(element)
            element = self.switchSmartFrogInstance(element)
            element = self.makeSureAboutHttpdTemplate(element)
        return element

    def addIRCNotification(self, element):
        """
        We add IRC notification :-)
        """
        publishers = element.find("project").find("publishers")
        old_irc_publisher = publishers.find("hudson.plugins.ircbot.IrcPublisher")
        if old_irc_publisher != None:
            publishers.remove(old_irc_publisher)
        irc_publisher_root = ET.fromstring(properties.IRC_PUBLISHER_XML)
        publishers.append(irc_publisher_root)
        return element

    def removeObsoleteShellTask(self, element):
        """
        We remove an obsolete ShellTask
        """
        builders = element.find("project").find("builders")
        shell_task = builders.find("hudson.tasks.Shell")
        if shell_task != None:
            builders.remove(shell_task)
        return element

    def switchSmartFrogInstance(self, element):
        """
        Meh, we kinda swap SmartFrog instances...
        """
        smartfrog_name = element.find("project").find("builders").find("builder.smartfrog.SmartFrogBuilder").find("smartFrogName")
        #if smartfrog_name.text is "SmartFrog 3.17 (DEBUG) mbabacek_fix":
        smartfrog_name.text = "SmartFrog 3.17 (DEBUG) mbabacek_playground"
        return element

    def makeSureAboutHttpdTemplate(self, element):
        """
        For RHEL, it should always be httpdPrepareTemplate
        """
        if element.tag.find("rhel") is not -1:
            sf_builder = element.find("project").find("builders").find("builder.smartfrog.SmartFrogBuilder")
            sf_script_source = sf_builder.find("sfScriptSource")
            smartfrog_script = ""
            if sf_script_source is not None:
                smartfrog_script = sf_script_source.find("scriptContent")
            else:
                smartfrog_script = sf_builder.find("scriptContent")
            smartfrog_script.text = smartfrog_script.text.replace("LAZY EwsPrepareModCluster ","LAZY httpdPrepareTemplate ")
        return element

