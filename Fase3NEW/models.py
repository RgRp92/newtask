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
    ist =[150,530,580,604,630,650,700,780,840,950]
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

    prb1 = 20
    prb2 = 20
    prb3 = 25
    prb4 = 20
    prb5 = 10
    prb6 = 5

    rs1_a1 = [18622, 18242, 18192, 18168, 18142, 18122, 18072, 17992, 17932, 17822]

    rs1_a2 = [17091, 16711, 16661, 16637, 16611, 16591, 16541, 16461, 16401, 16291]

    rs1_a3 = [19132, 18753, 18703, 18679, 18653, 18633, 18583, 18503, 18443, 18333]

    rs1_a4 = [21174, 20794, 20744, 20720, 20694, 20674, 20624, 20544, 20484, 20374]

    rs1_a5 = [23215, 22836, 22786, 22762, 22736, 22716, 22666, 22586, 22526, 22416]

    rs1_a6 = [25257, 24877, 24827, 24803, 24777, 24757, 24707, 24627, 24567, 24457]

    rdiff_1 = [3311, 261]
    rdiff_2 = [2931, 641]
    rdiff_3 = [2881, 691]
    rdiff_4 = [2857, 715]
    rdiff_5 = [2831, 741]
    rdiff_6 = [2811, 761]
    rdiff_7 = [2761, 811]
    rdiff_8 = [2681, 891]
    rdiff_9 = [2621, 951]
    rdiff_10 = [2511, 1061]

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

    # This is needed for the instructions
    rHL = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)



    # Define here the methods associated to Players
    # this method is needed to compute payoffs
    def set_payoff_rHL(self):
        #*******************************************
        # select random row and random outcome
        #*******************************************
        #
        self.participant.vars['rHL_row'] = random.randint(1,10)

        # select one row randomly for payment (from module random)
        self.participant.vars['rHL_random'] = random.randint(1,10)

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
                   self.rHL_10]


        # create a list with all choices of the player (see self)
        self.participant.vars['HL_choice_rs1'] = choices_rs1[self.participant.vars['rHL_row']-1]

        # select from the list the choice in correspondence to the randomly drawn row (notice the offset)
        # write it to participant.vars['HL_choice']

        #*******************************************
        # Compute here the payoffs
        #*******************************************
        if self.participant.vars['rHL_scenario'] <= 20:
            # if the random number is smaller equal than the random row
            if self.participant.vars['HL_choice_rs1'] == 1: #A
                # if the choice was A
                self.participant.vars['payoff_rHL'] = Constants.rs1_a1[self.participant.vars['rHL_row']-1]
                    # because HL_row is the same as p in the MPL
            else:
                self.participant.vars['payoff_rHL'] = Constants.rs1_b1[0]
        elif self.participant.vars['rHL_scenario'] > 20 and self.participant.vars['rHL_scenario'] <= 40:
            # if the random number is larger than the random row
            if self.participant.vars['HL_choice_rs1'] == 1 :#A
                    # if the choice was A
                self.participant.vars['payoff_rHL'] = Constants.rs1_a2[self.participant.vars['rHL_row']-1]
                    # because HL_row is the same as p in the MPL
            else:
                self.participant.vars['payoff_rHL'] = Constants.rs1_b1[1]
        elif self.participant.vars['rHL_scenario'] > 40 and self.participant.vars['rHL_scenario'] <= 65:
            # if the random number is larger than the random row
            if self.participant.vars['HL_choice_rs1'] == 1 :#A
                    # if the choice was A
                self.participant.vars['payoff_rHL'] = Constants.rs1_a3[self.participant.vars['rHL_row']-1]
                    # because HL_row is the same as p in the MPL
            else:
                self.participant.vars['payoff_rHL'] = Constants.rs1_b1[2]
        elif self.participant.vars['rHL_scenario'] > 65 and self.participant.vars['rHL_scenario'] <= 85:
            # if the random number is larger than the random row
            if self.participant.vars['HL_choice_rs1'] == 1 :#A
                    # if the choice was A
                self.participant.vars['payoff_rHL'] = Constants.rs1_a4[self.participant.vars['rHL_row']-1]
                    # because HL_row is the same as p in the MPL
            else:
                self.participant.vars['payoff_rHL'] = Constants.rs1_b1[3]
        elif self.participant.vars['rHL_scenario'] > 85 and self.participant.vars['rHL_scenario'] <= 95:
            # if the random number is larger than the random row
            if self.participant.vars['HL_choice_rs1'] == 1 :#A
                    # if the choice was A
                self.participant.vars['payoff_rHL'] = Constants.rs1_a5[self.participant.vars['rHL_row']-1]
                    # because HL_row is the same as p in the MPL
            else:
                self.participant.vars['payoff_rHL'] = Constants.rs1_b1[4]
        elif self.participant.vars['rHL_scenario'] > 95 and self.participant.vars['rHL_scenario'] <= 100:
            # if the random number is larger than the random row
            if self.participant.vars['HL_choice_rs1'] == 1 :#A
                    # if the choice was A
                self.participant.vars['payoff_rHL'] = Constants.rs1_a6[self.participant.vars['rHL_row']-1]
                    # because HL_row is the same as p in the MPL
            else:
                self.participant.vars['payoff_rHL'] = Constants.rs1_b1[5]


        self.payoff = self.participant.vars['payoff_rHL']
        # write the payoff to player.payoff