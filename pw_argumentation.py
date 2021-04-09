from mesa import Model
from mesa.time import RandomActivation
import sys
sys.path.append('D:\Documents\Cours\syst_multiagent\mesa_preference\mesa')
from communication.agent.CommunicatingAgent import CommunicatingAgent
from communication.message.MessageService import MessageService

from communication.preferences.Preferences import Preferences
from communication.preferences.CriterionName import CriterionName
from communication.preferences.CriterionValue import CriterionValue 
from communication.preferences.Item import Item 
from communication.preferences.Value import Value

from random import randrange

class ArgumentAgent(CommunicatingAgent):
    """ TestAgent which inherit from CommunicatingAgent.
    """
    def __init__(self, unique_id, model, name):
        super().__init__(unique_id, model, name)
        self.preference = None

    def step(self):
        super().step()

    def get_preference(self):
        return self.preference

    def generate_preferences(self):
        # To be completed
        self.preferences = Preferences()
        self.preferences.set_criterion_name_list([CriterionName.PRODUCTION_COST, CriterionName.ENVIRONMENT_IMPACT,
                                                  CriterionName.CONSUMPTION, CriterionName.DURABILITY, CriterionName.NOISE])
        for it in self.model.get_list_items() :
            for crit in self.preferences.get_criterion_name_list() :
                self.preferences.add_criterion_value(CriterionValue(it, crit,Value(randrange(5))))
     
class ArgumentModel(Model):
    
    """ ArgumentModel which inherit from Model.
    """
    def __init__(self):
        self.schedule = RandomActivation(self)
        self.__messages_service = MessageService(self.schedule)

        # To be completed
        
        self.list_items = []
        
        a = ArgumentAgent(next(), self, "alice")
        a.generate_preferences()
        self.schedule.add(a)
        
        b = ArgumentAgent(next(), self, "bob")
        b.generate_preferences()
        self.schedule.add(b)
        
        self.running = True

    def step(self):
        self.__messages_service.dispatch_messages()
        self.schedule.step()
        
    def get_list_items(self):
        return self.list_items


if __name__ == "__main__":
    argument_model = ArgumentModel()
    # To be completed
