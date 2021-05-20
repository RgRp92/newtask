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
    ist =[150,350,650,750,850,875,900,930,961,990,1020,1050,1080]
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
    prb2 = 23
    prb3 = 20
    prb4 = 12
    prb5 = 9
    prb6 = 6

    rs1_a1 = [18622, 18422,18122,18022,17922,17897,17872,17842,17811,17782,17752,17722,17692]

    rs1_a2 = [17091,16891,16591,16491,16391,16366,16341,16311,16280,16251,16221,16191,16161]

    rs1_a3 = [19133,18933,18633,18533,18433,18408,18383,18353,18322,18293,18263,18233,18203]

    rs1_a4 = [21174,20974,20674,20574,20474,20449,20424,20394,20363,20334,20304,20274,20244]

    rs1_a5 = [23216,23016,22716,22616,22516,22491,22466,22436,22405,22376,22346,22316,22286]

    rs1_a6 = [25257,25057,24757,24657,24557,24532,24507,24477,24446,24417,24387,24357,24327]

    rdiff_1 = [3311, 261]
    rdiff_2 = [3111, 461]
    rdiff_3 = [2811, 761]
    rdiff_4 = [2711, 861]
    rdiff_5 = [2611, 961]
    rdiff_6 = [2586, 986]
    rdiff_7 = [2561, 1011]
    rdiff_8 = [2531, 1041]
    rdiff_9 = [2500, 10721]
    rdiff_10 = [2471, 1101]
    rdiff_11 = [2441, 1131]
    rdiff_12 = [2411, 1161]
    rdiff_13 = [2381, 1191]

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
    rHL_13 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)

    # This is needed for the instructions
    rHL = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)



    # Define here the methods associated to Players
    # this method is needed to compute payoffs
    def set_payoff_rHL(self):
        #*******************************************
        # select random row and random outcome
        #*******************************************
        #
        self.participant.vars['rHL_row'] = random.randint(1,13)

        # select one row randomly for payment (from module random)
        self.participant.vars['rHL_random'] = random.randint(1,13)

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
                   self.rHL_10,self.rHL_11,self.rHL_12,self.rHL_13]


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
        elif self.participant.vars['rHL_scenario'] > 30 and self.participant.vars['rHL_scenario'] <= 53:
            # if the random number is larger than the random row
            if self.participant.vars['HL_choice_rs1'] == 1 :#A
                    # if the choice was A
                self.participant.vars['payoff_rHL'] = Constants.rs1_a2[self.participant.vars['rHL_row']-1]
                    # because HL_row is the same as p in the MPL
            else:
                self.participant.vars['payoff_rHL'] = Constants.rs1_b1[1]
        elif self.participant.vars['rHL_scenario'] > 53 and self.participant.vars['rHL_scenario'] <= 73:
            # if the random number is larger than the random row
            if self.participant.vars['HL_choice_rs1'] == 1 :#A
                    # if the choice was A
                self.participant.vars['payoff_rHL'] = Constants.rs1_a3[self.participant.vars['rHL_row']-1]
                    # because HL_row is the same as p in the MPL
            else:
                self.participant.vars['payoff_rHL'] = Constants.rs1_b1[2]
        elif self.participant.vars['rHL_scenario'] > 73 and self.participant.vars['rHL_scenario'] <= 85:
            # if the random number is larger than the random row
            if self.participant.vars['HL_choice_rs1'] == 1 :#A
                    # if the choice was A
                self.participant.vars['payoff_rHL'] = Constants.rs1_a4[self.participant.vars['rHL_row']-1]
                    # because HL_row is the same as p in the MPL
            else:
                self.participant.vars['payoff_rHL'] = Constants.rs1_b1[3]
        elif self.participant.vars['rHL_scenario'] > 85 and self.participant.vars['rHL_scenario'] <= 94:
            # if the random number is larger than the random row
            if self.participant.vars['HL_choice_rs1'] == 1 :#A
                    # if the choice was A
                self.participant.vars['payoff_rHL'] = Constants.rs1_a5[self.participant.vars['rHL_row']-1]
                    # because HL_row is the same as p in the MPL
            else:
                self.participant.vars['payoff_rHL'] = Constants.rs1_b1[4]
        elif self.participant.vars['rHL_scenario'] > 94 and self.participant.vars['rHL_scenario'] <= 100:
            # if the random number is larger than the random row
            if self.participant.vars['HL_choice_rs1'] == 1 :#A
                    # if the choice was A
                self.participant.vars['payoff_rHL'] = Constants.rs1_a6[self.participant.vars['rHL_row']-1]
                    # because HL_row is the same as p in the MPL
            else:
                self.participant.vars['payoff_rHL'] = Constants.rs1_b1[5]


        self.payoff = self.participant.vars['payoff_rHL']
        # write the payoff to player.payoff