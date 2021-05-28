from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import locale
locale.setlocale(locale.LC_ALL,'')


author = 'Ruggiero Rippo'

doc = """
    MPL risk elicitation à la Tanaka et al 2010
"""

import random

class Constants(BaseConstants):
    name_in_url = 'Fase2NEW'
    players_per_group = None
    num_rounds = 1
    # these are the lottery payoffs, f1 and f2 refer to lottery A and f3 and f4 to lottery B
    ##SERIE_1
    aex = 20943.67
    aaex=22518.42
    bex=18080.46
    bbex=23329.63

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

    s1_a1 = [18622,
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

    s1_a2 = [17091,
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

    s1_a3 = [19133,
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
18183,
             ]

    s1_a4 = [21174,
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

    s1_a5 = [23216,
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


    diff_1 = [3311, 261]
    diff_2 = [2961, 611]
    diff_3 = [2611, 961]
    diff_4 = [2581, 991]
    diff_5 = [2551, 1021]
    diff_6 = [2521, 1051]
    diff_7 = [2500, 1072]
    diff_8 = [2481, 1091]
    diff_9 = [2461, 1111]
    diff_10 = [2431, 1141]
    diff_11 = [2401, 1171]
    diff_12 = [2361, 1211]


    s1_b1 = [15311,17353,19394,21436,23477]



class Group(BaseGroup):
    pass

class Subsession(BaseSubsession):
    pass

class Player(BasePlayer):

    quiz = models.CharField(choices=[['1', '20444 €'], ['2', '16361 €'], ['2', '21436 €']],
                            widget=widgets.RadioSelectHorizontal,
                            label='In base alla figura mostrata, quale sarà il suo guadagno se la variazione sarà tra +1% e +10%?',
                             default="")

    quiz2 = models.CharField(choices=[['1', '20444 €'], ['2', '16361 €'], ['2', '21436 €']],
                             widget=widgets.RadioSelectHorizontal,
                             label='In base alla figura mostrata quale sarà il suo guadagno se la variazione sarà tra +1% e +10%?',
                            default="")


    # This is for main choices, each variable is one row in the choice table MPL
    HL_1 = models.IntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal,initial=0)
    HL_2 = models.IntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal,initial=0)
    HL_3 = models.IntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal,initial=0)
    HL_4 = models.IntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal,initial=0)
    HL_5 = models.IntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal,initial=0)
    HL_6 = models.IntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal,initial=0)
    HL_7 = models.IntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal,initial=0)
    HL_8 = models.IntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal,initial=0)
    HL_9 = models.IntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal,initial=0)
    HL_10 = models.IntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal,initial=0)
    HL_11 = models.IntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal,initial=0)
    HL_12 = models.IntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal,initial=0)

    HL = models.IntegerField(choices=[[1,'A'],[2,'B']],widget=widgets.RadioSelectHorizontal,initial=0)



    # Define here the methods associated to Players
    # this method is needed to compute payoffs
    def set_payoff_HL(self):
        #*******************************************
        # select random row and random outcome
        #*******************************************
        #
        self.participant.vars['HL_row'] = random.randint(1,12)

        # select one row randomly for payment (from module random)
        self.participant.vars['HL_random'] = random.randint(1,12)

        # select the number x that defines the outcome of the lottery (if x<=p, outcome is left f1 or f3, otherwise f2 or f4)
        self.participant.vars['HL_scenario'] = random.randint(1,100)

        # write it to participant.vars['HL_random']

        #*******************************************
        # select choices in correspondence to random row
        #*******************************************
        choices_s1 = [self.HL_1,
                   self.HL_2,
                   self.HL_3,
                   self.HL_4,
                   self.HL_5,
                   self.HL_6,
                   self.HL_7,
                   self.HL_8,
                   self.HL_9,
                   self.HL_10,
                   self.HL_11,self.HL_12]


        # create a list with all choices of the player (see self)
        self.participant.vars['HL_choice_s1'] = choices_s1[self.participant.vars['HL_row']-1]

        # select from the list the choice in correspondence to the randomly drawn row (notice the offset)
        # write it to participant.vars['HL_choice']

        #*******************************************
        # Compute here the payoffs
        #*******************************************
        if self.participant.vars['HL_scenario'] <= 30:
            # if the random number is smaller equal than the random row
            if self.participant.vars['HL_choice_s1'] == 1: #A
                # if the choice was A
                self.participant.vars['payoff_HL'] = Constants.s1_a1[self.participant.vars['HL_row']-1]
                    # because HL_row is the same as p in the MPL
            else:
                self.participant.vars['payoff_HL'] = Constants.s1_b1[0]
        elif self.participant.vars['HL_scenario'] > 30 and self.participant.vars['HL_scenario'] <= 54:
            # if the random number is larger than the random row
            if self.participant.vars['HL_choice_s1'] == 1 :#A
                    # if the choice was A
                self.participant.vars['payoff_HL'] = Constants.s1_a2[self.participant.vars['HL_row']-1]
                    # because HL_row is the same as p in the MPL
            else:
                self.participant.vars['payoff_HL'] = Constants.s1_b1[1]
        elif self.participant.vars['HL_scenario'] > 54 and self.participant.vars['HL_scenario'] <= 73:
            # if the random number is larger than the random row
            if self.participant.vars['HL_choice_s1'] == 1 :#A
                    # if the choice was A
                self.participant.vars['payoff_HL'] = Constants.s1_a3[self.participant.vars['HL_row']-1]
                    # because HL_row is the same as p in the MPL
            else:
                self.participant.vars['payoff_HL'] = Constants.s1_b1[2]
        elif self.participant.vars['HL_scenario'] > 73 and self.participant.vars['HL_scenario'] <= 88:
            # if the random number is larger than the random row
            if self.participant.vars['HL_choice_s1'] == 1 :#A
                    # if the choice was A
                self.participant.vars['payoff_HL'] = Constants.s1_a4[self.participant.vars['HL_row']-1]
                    # because HL_row is the same as p in the MPL
            else:
                self.participant.vars['payoff_HL'] = Constants.s1_b1[3]
        elif self.participant.vars['HL_scenario'] > 88 and self.participant.vars['HL_scenario'] <= 100:
            # if the random number is larger than the random row
            if self.participant.vars['HL_choice_s1'] == 1 :#A
                    # if the choice was A
                self.participant.vars['payoff_HL'] = Constants.s1_a5[self.participant.vars['HL_row']-1]
                    # because HL_row is the same as p in the MPL
            else:
                self.participant.vars['payoff_HL'] = Constants.s1_b1[4]


        self.payoff = self.participant.vars['payoff_HL']
        # write the payoff to player.payoff
