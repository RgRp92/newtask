from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Page0(Page):


    def is_displayed(self):
        return self.round_number == 1

class IstruzioniPage1(Page):
    form_model = 'player'

class IstruzioniPage2(Page):
    form_model = 'player'

class IstruzioniPage3(Page):
    form_model = 'player'
    def vars_for_template(self):
        var1 = Constants.var1*100
        var2 = Constants.var2*100
        var3 = Constants.var3*100
        var4 = Constants.var4 * 100
        var5 = Constants.var5 * 100
        var6 = Constants.var6 * 100
        prb1 = Constants.prb1
        prb2 = Constants.prb2
        prb3 = Constants.prb3
        prb4 = Constants.prb4
        prb5 = Constants.prb5
        prb6 = Constants.prb6

        return {
            'var1': var1,
            'var2': var2,
            'var3': var3,
            'var4': var4,
            'var5': var5,
            'var6': var6,
            'prb1': prb1,
            'prb2': prb2,
            'prb3': prb3,
            'prb4': prb4,
            'prb5': prb5,
            'prb6': prb6,

        }

class IstruzioniPage4(Page):
    form_model = 'player'

class EsempioPage1(Page):
# which forms are needed from class player
    form_model = 'player'
    def vars_for_template(self):
        # retrieve values from constants and store them in a dictionary
        var1 = Constants.var1 * 100
        var11 = Constants.var11 * 100
        var2 = Constants.var2 * 100
        var22 = Constants.var22 * 100
        var3 = Constants.var3 * 100
        var33 = Constants.var33 * 100
        var4 = Constants.var4 * 100
        var44 = Constants.var44 * 100
        var5 = Constants.var5 * 100
        var55 = Constants.var55 * 100
        var6 = Constants.var6 * 100
        var66 = Constants.var66 * 100
        prb1 = Constants.prb1
        prb2 = Constants.prb2
        prb3 = Constants.prb3
        prb4 = Constants.prb4
        prb5 = Constants.prb5
        prb6 = Constants.prb6
        return {
            'prb1': prb1,
            'prb2': prb2,
            'prb3': prb3,
            'prb4': prb4,
            'prb5': prb5,
            'prb6': prb6,
            'var1': var1,
            'var11': var11,
            'var2': var2,
            'var22': var22,
            'var3': var3,
            'var33': var33,
            'var4': var4,
            'var44': var44,
             'var5': var5,
            'var55': var55,
            'var6': var6,
             'var66': var66,
            'ist4': Constants.ist[3],
            'rs1_a1_4': Constants.rs1_a1[3],
            'rs1_a2_4': Constants.rs1_a2[3],
            'rs1_a3_4': Constants.rs1_a3[3],
            'rs1_a4_4': Constants.rs1_a4[3],
            'rs1_a5_4': Constants.rs1_a5[3],
            'rs1_a6_4': Constants.rs1_a6[3],
            'rs1_b1_1': Constants.rs1_b1[0],
            'rs1_b1_2': Constants.rs1_b1[1],
            'rs1_b1_3': Constants.rs1_b1[2],
            'rs1_b1_4': Constants.rs1_b1[3],
            'rs1_b1_5': Constants.rs1_b1[4],
            'rs1_b1_6': Constants.rs1_b1[5]

        }


    # values that are to be displayed (dictionary)
    # before moving to next page, compute payoffs (avoids that with refreshing payoffs are recomputed again)

class MyWaitPage(Page):
    form_model = 'player'

class HL_Page1(Page):
# which forms are needed from class player
    form_model = 'player'
    form_fields = ['rHL_1',
                   'rHL_2',
                   'rHL_3',
                   'rHL_4',
                   'rHL_5',
                   'rHL_6',
                   'rHL_7',
                   'rHL_8',
                   'rHL_9',
                   'rHL_10'
                   ] # all 10 options

    # values that are to be displayed (dictionary)
    def vars_for_template(self):
        # retrieve values from constants and store them in a dictionary
        var1 = Constants.var1 * 100
        var11 = Constants.var11 * 100
        var2 = Constants.var2 * 100
        var22 = Constants.var22 * 100
        var3 = Constants.var3 * 100
        var33 = Constants.var33 * 100
        var4 = Constants.var4 * 100
        var44 = Constants.var44 * 100
        var5 = Constants.var5 * 100
        var55 = Constants.var55 * 100
        var6 = Constants.var6 * 100
        var66 = Constants.var66 * 100
        prb1 = Constants.prb1
        prb2 = Constants.prb2
        prb3 = Constants.prb3
        prb4 = Constants.prb4
        prb5 = Constants.prb5
        prb6 = Constants.prb6
        return {
            'prb1': prb1,
            'prb2': prb2,
            'prb3': prb3,
            'prb4': prb4,
            'prb5': prb5,
            'prb6': prb6,
            'var1': var1,
            'var11': var11,
            'var2': var2,
            'var22': var22,
            'var3': var3,
            'var33': var33,
            'var4': var4,
            'var44': var44,
            'var5': var5,
            'var55': var55,
            'var6': var6,
            'var66': var66,
            'ist1': Constants.ist[0],
            'ist2': Constants.ist[1],
            'ist3': Constants.ist[2],
            'ist4': Constants.ist[3],
            'ist5': Constants.ist[4],
            'ist6': Constants.ist[5],
            'ist7': Constants.ist[6],
            'ist8': Constants.ist[7],
            'ist9': Constants.ist[8],
            'ist10': Constants.ist[9],

            'rs1_a1_1': Constants.rs1_a1[0],
            'rs1_a1_2': Constants.rs1_a1[1],
            'rs1_a1_3': Constants.rs1_a1[2],
            'rs1_a1_4': Constants.rs1_a1[3],
            'rs1_a1_5': Constants.rs1_a1[4],
            'rs1_a1_6': Constants.rs1_a1[5],
            'rs1_a1_7': Constants.rs1_a1[6],
            'rs1_a1_8': Constants.rs1_a1[7],
            'rs1_a1_9': Constants.rs1_a1[8],
            'rs1_a1_10': Constants.rs1_a1[9],
            'rs1_a2_1': Constants.rs1_a2[0],
            'rs1_a2_2': Constants.rs1_a2[1],
            'rs1_a2_3': Constants.rs1_a2[2],
            'rs1_a2_4': Constants.rs1_a2[3],
            'rs1_a2_5': Constants.rs1_a2[4],
            'rs1_a2_6': Constants.rs1_a2[5],
            'rs1_a2_7': Constants.rs1_a2[6],
            'rs1_a2_8': Constants.rs1_a2[7],
            'rs1_a2_9': Constants.rs1_a2[8],
            'rs1_a2_10': Constants.rs1_a2[9],
            'rs1_a3_1': Constants.rs1_a3[0],
            'rs1_a3_2': Constants.rs1_a3[1],
            'rs1_a3_3': Constants.rs1_a3[2],
            'rs1_a3_4': Constants.rs1_a3[3],
            'rs1_a3_5': Constants.rs1_a3[4],
            'rs1_a3_6': Constants.rs1_a3[5],
            'rs1_a3_7': Constants.rs1_a3[6],
            'rs1_a3_8': Constants.rs1_a3[7],
            'rs1_a3_9': Constants.rs1_a3[8],
            'rs1_a3_10': Constants.rs1_a3[9],
            'rs1_a4_1': Constants.rs1_a4[0],
            'rs1_a4_2': Constants.rs1_a4[1],
            'rs1_a4_3': Constants.rs1_a4[2],
            'rs1_a4_4': Constants.rs1_a4[3],
            'rs1_a4_5': Constants.rs1_a4[4],
            'rs1_a4_6': Constants.rs1_a4[5],
            'rs1_a4_7': Constants.rs1_a4[6],
            'rs1_a4_8': Constants.rs1_a4[7],
            'rs1_a4_9': Constants.rs1_a4[8],
            'rs1_a4_10': Constants.rs1_a4[9],
            'rs1_a5_1': Constants.rs1_a5[0],
            'rs1_a5_2': Constants.rs1_a5[1],
            'rs1_a5_3': Constants.rs1_a5[2],
            'rs1_a5_4': Constants.rs1_a5[3],
            'rs1_a5_5': Constants.rs1_a5[4],
            'rs1_a5_6': Constants.rs1_a5[5],
            'rs1_a5_7': Constants.rs1_a5[6],
            'rs1_a5_8': Constants.rs1_a5[7],
            'rs1_a5_9': Constants.rs1_a5[8],
            'rs1_a5_10': Constants.rs1_a5[9],
            'rs1_a6_1': Constants.rs1_a6[0],
            'rs1_a6_2': Constants.rs1_a6[1],
            'rs1_a6_3': Constants.rs1_a6[2],
            'rs1_a6_4': Constants.rs1_a6[3],
            'rs1_a6_5': Constants.rs1_a6[4],
            'rs1_a6_6': Constants.rs1_a6[5],
            'rs1_a6_7': Constants.rs1_a6[6],
            'rs1_a6_8': Constants.rs1_a6[7],
            'rs1_a6_9': Constants.rs1_a6[8],
            'rs1_a6_10': Constants.rs1_a6[9],

            'rs1_b1_1': Constants.rs1_b1[0],
            'rs1_b1_2': Constants.rs1_b1[1],
            'rs1_b1_3': Constants.rs1_b1[2],
            'rs1_b1_4': Constants.rs1_b1[3],
            'rs1_b1_5': Constants.rs1_b1[4],
            'rs1_b1_6': Constants.rs1_b1[5]
            }
    # before moving to next page, compute payoffs (avoids that with refreshing payoffs are recomputed again)


    def before_next_page(self):
    # built-in method
        self.player.set_payoff_rHL()# see in models in Player class
        self.participant.vars['ra1_value'] = Constants.rs1_a1[self.participant.vars['rHL_row'] - 1]
        self.participant.vars['ra2_value'] = Constants.rs1_a2[self.participant.vars['rHL_row'] - 1]
        self.participant.vars['ra3_value'] = Constants.rs1_a3[self.participant.vars['rHL_row'] - 1]
        self.participant.vars['ra4_value'] = Constants.rs1_a4[self.participant.vars['rHL_row'] - 1]
        self.participant.vars['ra5_value'] = Constants.rs1_a5[self.participant.vars['rHL_row'] - 1]
        self.participant.vars['ra6_value'] = Constants.rs1_a6[self.participant.vars['rHL_row'] - 1]

        self.participant.vars['rb1_value'] = Constants.rs1_b1[0]
        self.participant.vars['rb2_value'] = Constants.rs1_b1[1]
        self.participant.vars['rb3_value'] = Constants.rs1_b1[2]
        self.participant.vars['rb4_value'] = Constants.rs1_b1[3]
        self.participant.vars['rb5_value'] = Constants.rs1_b1[4]
        self.participant.vars['rb6_value'] = Constants.rs1_b1[5]

        self.participant.vars['var1'] = Constants.var1
        self.participant.vars['var11'] = Constants.var11
        self.participant.vars['var2'] = Constants.var2
        self.participant.vars['var22'] = Constants.var22
        self.participant.vars['var3'] = Constants.var3
        self.participant.vars['var33'] = Constants.var33
        self.participant.vars['var4'] = Constants.var4
        self.participant.vars['var44'] = Constants.var44
        self.participant.vars['var5'] = Constants.var5
        self.participant.vars['var55'] = Constants.var55
        self.participant.vars['var6'] = Constants.var6
        self.participant.vars['var66'] = Constants.var66

        self.participant.vars['prb1'] = Constants.prb1
        self.participant.vars['prb2'] = Constants.prb2
        self.participant.vars['prb3'] = Constants.prb3
        self.participant.vars['prb4'] = Constants.prb4
        self.participant.vars['prb5'] = Constants.prb5
        self.participant.vars['prb6'] = Constants.prb6

class OutcomeHL(Page):
# values needed to inform subjects about the actual outcome
    def vars_for_template(self):
            # retrieve values from participant.vars and store them in a dictionary
            return{
            'payoff_rHL': self.player.participant.vars['payoff_rHL'],#payoff
            'rrow': self.player.participant.vars['rHL_row'], # randomly chosen row
            'rvalue': self.participant.vars['rHL_random'],# randomly chosen value to define outcome
            'rvalue2': self.participant.vars['rHL_scenario'],
            'rchoice': self.participant.vars['HL_choice_rs1'],# actual choice
            # outcomes of the selected row
            'ra1_value': Constants.rs1_a1[self.participant.vars['rHL_row'] - 1],
            'ra2_value': Constants.rs1_a2[self.participant.vars['rHL_row'] - 1],
            'ra3_value': Constants.rs1_a3[self.participant.vars['rHL_row'] - 1],
            'ra4_value': Constants.rs1_a4[self.participant.vars['rHL_row'] - 1],
            'ra5_value': Constants.rs1_a5[self.participant.vars['rHL_row'] - 1],
            'ra6_value': Constants.rs1_a6[self.participant.vars['rHL_row'] - 1],

            'rb1_value': Constants.rs1_b1[0],
            'rb2_value': Constants.rs1_b1[1],
            'rb3_value': Constants.rs1_b1[2],
            'rb4_value': Constants.rs1_b1[3],
            'rb5_value': Constants.rs1_b1[4],
            'rb6_value': Constants.rs1_b1[5],

            'p_A_1': self.participant.vars['rHL_row'],
            'p_A_2': 10-self.participant.vars['rHL_row'],
            'p_B_1': self.participant.vars['rHL_row'],
            'p_B_2': 10-self.participant.vars['rHL_row'],
            'ist_value':Constants.ist[self.participant.vars['rHL_row'] - 1],
            'var1': -Constants.var1 * 100,
            'var11': -Constants.var11 * 100,
            'var2': -Constants.var2 * 100,
            'var22': -Constants.var22 * 100,
            'var3': -Constants.var3 * 100,
            'var33': Constants.var33 * 100,
            'var4': +Constants.var44 * 100,
            'var44': +Constants.var44 * 100,
            'var5': +Constants.var5 * 100,
            'var55': +Constants.var55 * 100,
            'var6': +Constants.var6 * 100,
            'var66': +Constants.var5 * 100,
            }
    def before_next_page(self):
        self.participant.vars['rist_value'] = Constants.ist[self.participant.vars['rHL_row'] - 1]


# the coreography of pages
page_sequence = [
                    Page0,
                    IstruzioniPage1,
                    IstruzioniPage2,
                    IstruzioniPage4,
                    EsempioPage1,
                    MyWaitPage,
                    HL_Page1,
                    OutcomeHL
]
