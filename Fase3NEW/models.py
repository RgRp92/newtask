from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Ruggiero Rippo'

doc = """
    MPL risk elicitation à la Tanaka et al 2010
"""

import random

class Constants(BaseConstants):
    name_in_url = 'Fase3NEW'
    players_per_group = None
    num_rounds = 1
    # these are the lottery payoffs, f1 and f2 refer to lottery A and f3 and f4 to lottery B
    ist =[150,500,850,880,910,940,961,980,1000,1030,1060,1100]
    var1 = 0.30
    var11 = 0.20

    var2 = 0.19
    var22 = 0.10

    var3 = 0.09
    var33 = 0.00

    var4 = 0.01
    var44 = 0.10

    var5 = 0.11
    var55 = 0.20

    var6 = 0.21
    var66 = 0.30

    prb1 = 30
    prb2 = 24
    prb3 = 19
    prb4 = 15
    prb5 = 12


    rs1_a1 = [18622,
18272,
17922,
17892,
17862,
17832,
17811,
17792,
17772,
17742,
17712,
17672]

    rs1_a2 = [17091,
16741,
16391,
16361,
16331,
16301,
16280,
16261,
16241,
16211,
16181,
16141]

    rs1_a3 = [19133,
18783,
18433,
18403,
18373,
18343,
18322,
18303,
18283,
18253,
18223,
18183]

    rs1_a4 = [21174,
20824,
20474,
20444,
20414,
20384,
20363,
20344,
20324,
20294,
20264,
20224]

    rs1_a5 = [23216,
22866,
22516,
22486,
22456,
22426,
22405,
22386,
22366,
22336,
22306,
22266]

    rdiff_1 = [3311, 261]
    rdiff_2 = [2961, 611]
    rdiff_3 = [2611, 961]
    rdiff_4 = [2581, 991]
    rdiff_5 = [2551, 1021]
    rdiff_6 = [2521, 1051]
    rdiff_7 = [2500, 1072]
    rdiff_8 = [2481, 1091]
    rdiff_9 = [2461, 1111]
    rdiff_10 = [2431, 1141]
    rdiff_11 = [2401, 1171]
    rdiff_12 = [2361, 1211]


    rs1_b1 = [15311,17353,19394,21436,23477,25519]

class Group(BaseGroup):
    pass

class Subsession(BaseSubsession):
    pass

class Player(BasePlayer):
    # This is for main choices, each variable is one row in the choice table MPL
    rHL_1 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    rHL_2 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    rHL_3 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    rHL_4 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    rHL_5 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    rHL_6 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    rHL_7 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    rHL_8 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    rHL_9 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    rHL_10 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    rHL_11 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    rHL_12 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)

    # This is needed for the instructions
    rHL = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)



    # Define here the methods associated to Players
    # this method is needed to compute payoffs
    def set_payoff_rHL(self):
        #*******************************************
        # select random row and random outcome
        #*******************************************
        #
        self.participant.vars['rHL_row'] = random.randint(1,12)

        # select one row randomly for payment (from module random)
        self.participant.vars['rHL_random'] = random.randint(1,12)

        # select the number x that defines the outcome of the lottery (if x<=p, outcome is left f1 or f3, otherwise f2 or f4)
        self.participant.vars['rHL_scenario'] = random.randint(1,100)

        # write it to participant.vars['HL_random']

        #*******************************************
        # select choices in correspondence to random row
        #*******************************************
        choices_rs1 = [self.rHL_1,
                   self.rHL_2,
                   self.rHL_3,
                   self.rHL_4,
                   self.rHL_5,
                   self.rHL_6,
                   self.rHL_7,
                   self.rHL_8,
                   self.rHL_9,
                   self.rHL_10,self.rHL_11,self.rHL_12]


        # create a list with all choices of the player (see self)
        self.participant.vars['HL_choice_rs1'] = choices_rs1[self.participant.vars['rHL_row']-1]

        # select from the list the choice in correspondence to the randomly drawn row (notice the offset)
        # write it to participant.vars['HL_choice']

        #*******************************************
        # Compute here the payoffs
        #*******************************************
        if self.participant.vars['rHL_scenario'] <= 30:
            # if the random number is smaller equal than the random row
            if self.participant.vars['HL_choice_rs1'] == 1: #A
                # if the choice was A
                self.participant.vars['payoff_rHL'] = Constants.rs1_a1[self.participant.vars['rHL_row']-1]
                    # because HL_row is the same as p in the MPL
            else:
                self.participant.vars['payoff_rHL'] = Constants.rs1_b1[0]
        elif self.participant.vars['rHL_scenario'] > 30 and self.participant.vars['rHL_scenario'] <= 54:
            # if the random number is larger than the random row
            if self.participant.vars['HL_choice_rs1'] == 1 :#A
                    # if the choice was A
                self.participant.vars['payoff_rHL'] = Constants.rs1_a2[self.participant.vars['rHL_row']-1]
                    # because HL_row is the same as p in the MPL
            else:
                self.participant.vars['payoff_rHL'] = Constants.rs1_b1[1]
        elif self.participant.vars['rHL_scenario'] > 54 and self.participant.vars['rHL_scenario'] <= 73:
            # if the random number is larger than the random row
            if self.participant.vars['HL_choice_rs1'] == 1 :#A
                    # if the choice was A
                self.participant.vars['payoff_rHL'] = Constants.rs1_a3[self.participant.vars['rHL_row']-1]
                    # because HL_row is the same as p in the MPL
            else:
                self.participant.vars['payoff_rHL'] = Constants.rs1_b1[2]
        elif self.participant.vars['rHL_scenario'] > 73 and self.participant.vars['rHL_scenario'] <= 88:
            # if the random number is larger than the random row
            if self.participant.vars['HL_choice_rs1'] == 1 :#A
                    # if the choice was A
                self.participant.vars['payoff_rHL'] = Constants.rs1_a4[self.participant.vars['rHL_row']-1]
                    # because HL_row is the same as p in the MPL
            else:
                self.participant.vars['payoff_rHL'] = Constants.rs1_b1[3]
        elif self.participant.vars['rHL_scenario'] > 88 and self.participant.vars['rHL_scenario'] <= 100:
            # if the random number is larger than the random row
            if self.participant.vars['HL_choice_rs1'] == 1 :#A
                    # if the choice was A
                self.participant.vars['payoff_rHL'] = Constants.rs1_a5[self.participant.vars['rHL_row']-1]
                    # because HL_row is the same as p in the MPL
            else:
                self.participant.vars['payoff_rHL'] = Constants.rs1_b1[4]


        self.payoff = self.participant.vars['payoff_rHL']
        # write the payoff to player.payoff