#!/usr/bin/env python3

from communication.arguments.Comparison import Comparison
from communication.arguments.CoupleValue import CoupleValue
from communication.preferences.Preferences import Preferences
from communication.preferences.Item import Item
from communication.preferences.Value import Value


class Argument:
    """Argument class.
    This class implements an argument used in the negotiation.

    attr:
        decision:
        item:
        comparison_list:
        couple_values_list:
    """

    def __init__(self, boolean_decision, item):
        """Creates a new Argument.
        """
        self.__decision = boolean_decision
        self.__item = item.get_name()
        self.__comparison_list = []
        self.__couple_values_list = []

    def add_premiss_comparison(self, criterion_name_1, criterion_name_2):
        """Adds a premiss comparison in the comparison list.
        """
        self.__comparison_list.append(
            Comparison(criterion_name_1, criterion_name_2))

    def add_premiss_couple_values(self, criterion_name, value):
        """Add a premiss couple values in the couple values list.
        """
        self.__couple_values_list.append(CoupleValue(criterion_name, value))

    def List_supporting_proposal(self, item: Item, preferences: Preferences):
        """Generate a list of premisses which can be used to support an item
        :param item: Item - name of the item
        :return: list of all premisses PRO an item (sorted by order of importance based on agent's preferences)
        """
        # To be completed: Done
        pro_proposal = []
        for criterion_name in preferences.get_criterion_name_list():
            # as stated in the exercise statement
            if preferences.get_value(item, criterion_name) >= Value.GOOD:
                pro_proposal.append(criterion_name)
        return pro_proposal

    def List_attacking_proposal(self, item, preferences: Preferences):
        """Generate a list of premisses which can be used to attack an item
        :param item: Item - name of the item
        :return: list of all premisses CON an item (sorted by order of importance based on preferences)
        """
        # To be completed: Done
        con_proposal = []
        for criterion_name in preferences.get_criterion_name_list():
            # as stated in the exercise statement
            if preferences.get_value(item, criterion_name) <= Value.BAD:
                con_proposal.append(criterion_name)
        return con_proposal
