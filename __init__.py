"""
skill-lifx: A Mycroft skill to control Lifx lights
Copyright (C) 2018  Anthony DiGiovanni

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import json
import sys

from adapt.intent import IntentBuilder
from adapt.engine import IntentDeterminationEngine
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG, getLogger
from mycroft import MycroftSkill, intent_file_handler
from padatious import IntentContainer

from pifx import PIFX

__author__ = 'GotTheNumbers'

#start logging
LOGGER = getLogger(__name__)

token = 'c399ab2247f132823d33749fee694ecbfbcac416de33b471aa918b30bb1fc436'

# Each skill is contained within its own class, which inherits base methods
# from the MycroftSkill class.  You extend this class as shown below.
class LifxSkill(MycroftSkill):
    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(LifxSkill, self).__init__(name="LifxSkill")

    def initialize(self):
        #check if the token is set
        if len(token) == 0:
            self.speak_dialog("please.add.access.token")
            return
    #     engine = IntentDeterminationEngine()
    #     #define lifx
    #     lifx_keyword = ["turn"]
    #     for lk in lifx_keyword:
    #         engine.register_entity(lk, "LifxKeyword")
    #     lifx_verbs = ["on", "off"]
    #     for lv in lifx_verbs:
    #         engine.register_entity(lv, "LifxVerb")
    #     device_names = ["kitchen", "lamp"]
    #     for dv in device_names:
    #         engine.register_entity(dv, "DeviceName")
    #
    #     lifx_intent = IntentBuilder("LifxIntent")\
    #         .require("LifxKeyword")\
    #         .require("LifxVerb")\
    #         .require("DeviceName")\
    #         .build()
    #     engine.register_intent_parser(lifx_intent)
    #
    #     self.register_intent(lifx_intent, self.handle_lifx_intent)
    #
    # def handle_lifx_intent(self, message):
    #     self.speak("THIS IS THE LIFX HANDLER!")

    # The ON intent handler
    @intent_handler(IntentBuilder("OnIntent").require("OnKeyword"))
    def handle_on_intent(self, message):
        self.speak(str(message.data))
        p = PIFX(self.settings["Token"])
        p.set_state(power="on")
        self.speak_dialog("on")

    # The OFF intent handler
    @intent_handler(IntentBuilder("OffIntent").require("OffKeyword"))
    def handle_off_intent(self, message):
        p = PIFX(self.settings["Token"])
        p.set_state(power="off")
        self.speak_dialog("off")


    # The "stop" method defines what Mycroft does when told to stop
    def stop(self):
        return True

# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
    return LifxSkill()
