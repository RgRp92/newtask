from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import random

class NotWinner(Page):


    def vars_for_template(self):
        return {
        "winners": self.session.vars["winners"],
        'app' : self.session.vars["app"],
        'id':   self.player.id_in_group
        }

    def is_displayed(self):
        return self.player.id_in_group not in self.session.vars["winners"]

class Winner(Page):

    def vars_for_template(self):
        return {
        "winners": self.session.vars['winners'],
        'app' : self.session.vars["app"],
        'id':   self.player.id_in_group
        }

    def is_displayed(self):
        return self.player.id_in_group in self.session.vars["winners"]

class ResultsWaitPage(WaitPage):
    pass

class Fase1(Page):
    def vars_for_template(self):
        return{
        "beliefs": self.participant.vars["beliefs_results"],
        "w_amt": self.participant.vars["w_amt"],
        "nw_bin": self.participant.vars["nw_bin"]
        }

    def is_displayed(self):
        return self.session.vars["app"] == 1 and self.player.id_in_group in self.session.vars["winners"]

    def before_next_page(self):
        self.player.payoff = round(self.participant.vars["w_amt"],2)

class Fase2(Page):
    def vars_for_template(self):
        payoff_HLc = round((self.player.participant.vars['payoff_HL']/1000) * (1.06),2)
        # retrieve values from participant.vars and store them in a dictionary
        return {
            'payoff_HL': self.player.participant.vars['payoff_HL'],
            'payoff_HLc':payoff_HLc, # payoff
            'row': self.player.participant.vars['HL_row'],  # randomly chosen row
            'value': self.participant.vars['HL_random'],  # randomly chosen value to define outcome
            'choice': self.participant.vars['HL_choice_s1'],  # actual choice
            # outcomes of the selected row
            'a1_value': self.participant.vars['a1_value'],
            'a2_value': self.participant.vars['a2_value'],
            'a3_value': self.participant.vars['a3_value'],
            'a4_value': self.participant.vars['a4_value'],
            'a5_value': self.participant.vars['a5_value'],
            'b1_value':self.participant.vars['b1_value'],
            'b2_value': self.participant.vars['b2_value'],
            'b3_value': self.participant.vars['b3_value'],
            'b4_value': self.participant.vars['b4_value'],
            'b5_value': self.participant.vars['b5_value'],
            'p_A_1': self.participant.vars['HL_row'],
            'p_A_2': 10 - self.participant.vars['HL_row'],
            'p_B_1': self.participant.vars['HL_row'],
            'p_B_2': 10 - self.participant.vars['HL_row'],
            'var1' : self.participant.vars['var1']*100,
            'var11' : self.participant.vars['var11']*100,
            'var2': self.participant.vars['var2']*100,
            'var22': self.participant.vars['var22']*100,
            'var3': self.participant.vars['var3']*100,
            'var33': self.participant.vars['var33']*100,
            'var4': self.participant.vars['var4']*100,
            'var44': self.participant.vars['var44']*100,
            'var5': self.participant.vars['var5']*100,
            'var55': self.participant.vars['var55']*100,
            'ist_value': self.participant.vars['ist_value']
        }

    def is_displayed(self):
        return self.session.vars["app"] == 2 and self.player.id_in_group in self.session.vars["winners"]

    def before_next_page(self):
        self.player.payoff = round((self.player.participant.vars['payoff_HL']/1000) * (1.06),2)

class Fase3(Page):
    def vars_for_template(self):
        payoff_rHLc = round((self.player.participant.vars['payoff_rHL']/1000) * (1.06),2)
        # retrieve values from participant.vars and store them in a dictionary
            # retrieve values from participant.vars and store them in a dictionary
        return {
                'payoff_rHL': self.player.participant.vars['payoff_rHL'],
                'payoff_rHLc': payoff_rHLc,  # payoff
                'rrow': self.player.participant.vars['rHL_row'],  # randomly chosen row
                'rvalue': self.participant.vars['rHL_random'],  # randomly chosen value to define outcome
                'rchoice': self.participant.vars['HL_choice_rs1'],  # actual choice
                # outcomes of the selected row
                'ra1_value': self.participant.vars['ra1_value'],
                'ra2_value': self.participant.vars['ra2_value'],
                'ra3_value': self.participant.vars['ra3_value'],
                'ra4_value': self.participant.vars['ra4_value'],
                'ra5_value': self.participant.vars['ra5_value'],
                'rb1_value': self.participant.vars['rb1_value'],
                'rb2_value': self.participant.vars['rb2_value'],
                'rb3_value': self.participant.vars['rb3_value'],
                'rb4_value': self.participant.vars['rb4_value'],
                'rb5_value': self.participant.vars['rb5_value'],
                'p_A_1': self.participant.vars['rHL_row'],
                'p_A_2': 10 - self.participant.vars['rHL_row'],
                'p_B_1': self.participant.vars['rHL_row'],
                'p_B_2': 10 - self.participant.vars['rHL_row'],
                'var1': self.participant.vars['var1'] * 100,
                'var11': self.participant.vars['var11'] * 100,
                'var2': self.participant.vars['var2'] * 100,
                'var22': self.participant.vars['var22'] * 100,
                'var3': self.participant.vars['var3'] * 100,
                'var33': self.participant.vars['var33'] * 100,
                'var4': self.participant.vars['var4'] * 100,
                'var44': self.participant.vars['var44'] * 100,
                'var5': self.participant.vars['var5'] * 100,
                'var55': self.participant.vars['var55'] * 100,

                'rist_value': self.participant.vars['rist_value'],
                'prb1': self.participant.vars['prb1'],
                'prb2': self.participant.vars['prb2'],
                'prb3': self.participant.vars['prb3'],
                'prb4': self.participant.vars['prb4'],
                'prb5': self.participant.vars['prb5'],
        }

    def is_displayed(self):
        return self.session.vars["app"] == 3 and self.player.id_in_group in self.session.vars["winners"]

    def before_next_page(self):
        self.player.payoff = round((self.player.participant.vars['payoff_rHL']/1000) * (1.06),2)


class goodbye(Page):
    form_model = 'player'

    def vars_for_template(self):
        return {
        'id':   self.player.id_in_group
        }

page_sequence = [NotWinner, Winner, Fase1, Fase2, Fase3, goodbye]
