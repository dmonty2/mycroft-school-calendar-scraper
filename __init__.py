# Mycroft skill to read the blocks at brock

from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler
import feedparser
import re
import datetime

class BrockBlocks(MycroftSkill):
    def __init__(self):
        """ first constructed for variables, setup actions """
        super().__init__()
        self.learning = True

    def initialize(self):
        """ final setup for skills. invoced after skill are constructioned."""

    @intent_handler('WhatAreTodaysBlocks.intent')
    def handle_todays_blocks_intent(self, message):
        self.speak(blocks)
        myDate = '{dt.month}/{dt.day}/{dt.year}'.format(dt = datetime.datetime.now())
        feed = feedparser.parse('/home/mycroft/rss-new.rss')
        for item in feed.entries:
            if re.search("\("+myDate+"\)", item.title):
                output = re.sub(" \("+myDate+"\)", "", item.title)
                if (len(output) == 4):
                    self.speak( output[0] + ". " + output[1] + ". " + output[2] + ". " + output[3] + "." )
                else:
                    self.speak( output )

