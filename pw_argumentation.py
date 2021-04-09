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

from random import randrange, shuffle

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
        self.preference = Preferences()
        self.preference.set_criterion_name_list(shuffle([CriterionName.PRODUCTION_COST, CriterionName.ENVIRONMENT_IMPACT,
                                                  CriterionName.CONSUMPTION, CriterionName.DURABILITY, CriterionName.NOISE]))
        for it in self.model.get_list_items() :
            for crit in self.preference.get_criterion_name_list() :
                self.preference.add_criterion_value(CriterionValue(it, crit,Value(randrange(5))))
     
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
    agent0 = argument_model.schedule.agents[0]
    agent1 = argument_model.schedule.agents[1]

    assert(agent0.get_name() == "alice")
    assert(agent1.get_name() == "bob")
    print("*     get_name() => OK")

    agent0.send_message(Message("alice", "bob", MessagePerformative.PROPOSE, argument_model.get_list_items()[0]))
    new_msg = agent1.get_new_messages()[0]
    perf = new_msg.get_performative()
    item = new_msg.get_content()
    if agent1.preference.is_item_among_top_10_percent(item, argument_model.get_list_items()) :
        agent1.send_message(Message("bob", "alice", MessagePerformative.ACCEPT, item))
    else :
        agent1.send_message(Message("bob", "alice", MessagePerformative.ASK_WHY, item))
