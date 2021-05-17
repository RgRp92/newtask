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

    s1_a1 = [18623,18243,18193,18169,18143,18123,18073,17993,17933,17823]

    s1_a2 = [17092,16712,16662,16638,16612,16592,16542,16462,16402,16292]

    s1_a3 = [19133,18753,18703,18679,18653,18633,18583,18503,18443,18333]

    s1_a4 = [21174,20794,20744,20720,20694,20674,20624,20544,20484,20374]

    s1_a5 = [23216,22836,22785,22761,22735,22715,22665,22585,22525,22415]

    s1_a6 = [25257,24877,24827,24803,24777,24757,24707,24627,24567,24457]

    diff_1 = [3311, 261]
    diff_2 = [2931, 641]
    diff_3 = [2881, 691]
    diff_4 = [2857, 715]
    diff_5 = [2831, 741]
    diff_6 = [2811, 761]
    diff_7 = [2761, 811]
    diff_8 = [2681, 891]
    diff_9 = [2621, 951]
    diff_10 = [2511, 1061]

    s1_b1 = [15311,17353,19394,21436,23477,25519]



class Group(BaseGroup):
    pass

class Subsession(BaseSubsession):
    pass

class Player(BasePlayer):

    quiz = models.CharField(choices=[['1', '€ 20720'], ['2', '€ 21436'], ['2', '€ 18168']],
                            widget=widgets.RadioSelectHorizontal,
                            label='In base alla figura mostrata, quale sarà il vostro guadagno se la variazione sarà del + 2%?',
                            blank=True, default="")

    quiz2 = models.CharField(choices=[['1', '€ 20720'], ['2', '€ 21436'], ['2', '€ 18168']],
                             widget=widgets.RadioSelectHorizontal,
                             label='In base alla figura mostrata quale sarà il vostro guadagno se la variazione sarà del +2%?',
                             blank=True, default="")

    quiz3 = models.CharField(choices=[['2', '€ 20720'], ['1', '€ 19394'], ['2', '€ 25518']],
                            widget=widgets.RadioSelectHorizontal,
                            label='In base alla figura mostrata quale sarà il vostro guadagno se la variazione sarà del - 8%?',
                            blank=True, default="")
    quiz4 = models.CharField(choices=[['2', '€ 20720'], ['1', '€ 19394'], ['2', '€ 25518']],
                             widget=widgets.RadioSelectHorizontal,
                             label='In base alla figura mostrata quale sarà il vostro guadagno se la variazione sarà del  -8%?',
                             blank=True, default="")

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

    HL = models.IntegerField(choices=[[1,'A'],[2,'B']],widget=widgets.RadioSelectHorizontal,initial=0)



    # Define here the methods associated to Players
    # this method is needed to compute payoffs
    def set_payoff_HL(self):
        #*******************************************
        # select random row and random outcome
        #*******************************************
        #
        self.participant.vars['HL_row'] = random.randint(1,10)

        # select one row randomly for payment (from module random)
        self.participant.vars['HL_random'] = random.randint(1,10)

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
                   self.HL_10]


        # create a list with all choices of the player (see self)
        self.participant.vars['HL_choice_s1'] = choices_s1[self.participant.vars['HL_row']-1]

        # select from the list the choice in correspondence to the randomly drawn row (notice the offset)
        # write it to participant.vars['HL_choice']

        #*******************************************
        # Compute here the payoffs
        #*******************************************
        if self.participant.vars['HL_scenario'] <= 20:
            # if the random number is smaller equal than the random row
            if self.participant.vars['HL_choice_s1'] == 1: #A
                # if the choice was A
                self.participant.vars['payoff_HL'] = Constants.s1_a1[self.participant.vars['HL_row']-1]
                    # because HL_row is the same as p in the MPL
            else:
                self.participant.vars['payoff_HL'] = Constants.s1_b1[0]
        elif self.participant.vars['HL_scenario'] > 20 and self.participant.vars['HL_scenario'] <= 40:
            # if the random number is larger than the random row
            if self.participant.vars['HL_choice_s1'] == 1 :#A
                    # if the choice was A
                self.participant.vars['payoff_HL'] = Constants.s1_a2[self.participant.vars['HL_row']-1]
                    # because HL_row is the same as p in the MPL
            else:
                self.participant.vars['payoff_HL'] = Constants.s1_b1[1]
        elif self.participant.vars['HL_scenario'] > 40 and self.participant.vars['HL_scenario'] <= 65:
            # if the random number is larger than the random row
            if self.participant.vars['HL_choice_s1'] == 1 :#A
                    # if the choice was A
                self.participant.vars['payoff_HL'] = Constants.s1_a3[self.participant.vars['HL_row']-1]
                    # because HL_row is the same as p in the MPL
            else:
                self.participant.vars['payoff_HL'] = Constants.s1_b1[2]
        elif self.participant.vars['HL_scenario'] > 65 and self.participant.vars['HL_scenario'] <= 85:
            # if the random number is larger than the random row
            if self.participant.vars['HL_choice_s1'] == 1 :#A
                    # if the choice was A
                self.participant.vars['payoff_HL'] = Constants.s1_a4[self.participant.vars['HL_row']-1]
                    # because HL_row is the same as p in the MPL
            else:
                self.participant.vars['payoff_HL'] = Constants.s1_b1[3]
        elif self.participant.vars['HL_scenario'] > 85 and self.participant.vars['HL_scenario'] <= 95:
            # if the random number is larger than the random row
            if self.participant.vars['HL_choice_s1'] == 1 :#A
                    # if the choice was A
                self.participant.vars['payoff_HL'] = Constants.s1_a5[self.participant.vars['HL_row']-1]
                    # because HL_row is the same as p in the MPL
            else:
                self.participant.vars['payoff_HL'] = Constants.s1_b1[4]
        elif self.participant.vars['HL_scenario'] > 95 and self.participant.vars['HL_scenario'] <= 100:
            # if the random number is larger than the random row
            if self.participant.vars['HL_choice_s1'] == 1 :#A
                    # if the choice was A
                self.participant.vars['payoff_HL'] = Constants.s1_a6[self.participant.vars['HL_row']-1]
                    # because HL_row is the same as p in the MPL
            else:
                self.participant.vars['payoff_HL'] = Constants.s1_b1[5]


        self.payoff = self.participant.vars['payoff_HL']
        # write the payoff to player.payoff
