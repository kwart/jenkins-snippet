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

