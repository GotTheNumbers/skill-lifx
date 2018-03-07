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

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG

from pifx import PIFX

__author__ = 'GotTheNumbers'

# Each skill is contained within its own class, which inherits base methods
# from the MycroftSkill class.  You extend this class as shown below.

class LifxSkill(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(LifxSkill, self).__init__(name="LifxSkill")

    @intent_handler(IntentBuilder("OnIntent").require("OnKeyword"))
    def handle_on_intent(self, message):
        if len(self.settings["Token"]) == 0:
            self.speak_dialog("please.add.access.token")
            return
        p = PIFX(self.settings["Token"])
        p.set_state(power="on")
        self.speak_dialog("on")

    # The "stop" method defines what Mycroft does when told to stop during
    # the skill's execution. In this case, since the skill's functionality
    # is extremely simple, there is no need to override it.  If you DO
    # need to implement stop, you should return True to indicate you handled
    # it.
    #
    # def stop(self):
    #    return False

# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
    return LifxSkill()
