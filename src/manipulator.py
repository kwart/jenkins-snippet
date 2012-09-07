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
        element = self.addIRCNotification(element)
        element = self.removeObsoleteShellTask(element)
        element = self.switchSmartFrogInstance(element)
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

