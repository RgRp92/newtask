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

    s1_a1 = [18622.49,18242.49,18192.49,18168.49,18142.49,18122.49,18072.49,17992.49,17932.49,17822.49]

    s1_a2 = [17091.38,16711.38,16661.38,16637.38,16611.38,16591.38,16541.38,16461.38,16401.38,16291.38]

    s1_a3 = [19132.86,18752.86,18702.86,18678.86,18652.86,18632.86,18582.86,18502.86,18442.86,18332.86]

    s1_a4 = [21174.34,20794.34,20744.34,20720.34,20694.34,20674.34,20624.34,20544.34,20484.34,20374.34]

    s1_a5 = [23215.83,22835.83,22785.83,22761.83,22735.83,22715.83,22665.83,22585.83,22525.83,22415.83]

    s1_a6 = [25257.31,24877.31,24827.31,24803.31,24777.31,24757.31,24707.31,24627.31,24567.31,24457.31]



    s1_b1 = [15311.11,17352.59,19394.07,21435.55,23477.04,25518.52]



class Group(BaseGroup):
    pass

class Subsession(BaseSubsession):
    pass

class Player(BasePlayer):
    quiz = models.CharField(choices=[['1', '€ 20720.34'], ['0', '€ 21435.55'], ['2', '€ 18168.49']],
                            widget=widgets.RadioSelectHorizontal,
                            label='1. In base alla figura mostrata quale sarà il vostro guadagno se la variazione sarà del + 2%',
                            blank=True, default="")
    quiz2 = models.CharField(choices=[['0', '€ 15311.11'], ['2', '€ 20720.34'],['1', '€ 18168.49']],
                             widget=widgets.RadioSelectHorizontal,
                             label='2.In base alla figura mostrata quale sarà il vostro guadagno se la variazione sarà del - 20%',
                             blank=True, default="")

    quiz3 = models.CharField(choices=[['0', '€ 20720.34'], ['1', '€ 19394.07'], ['2', '€ 25518.52']],
                            widget=widgets.RadioSelectHorizontal,
                            label='1. In base alla figura mostrata quale sarà il vostro guadagno se la variazione sarà del - 8%',
                            blank=True, default="")
    quiz4 = models.CharField(choices=[['0', '€ 18072.49'], ['2', '€ 20624.34'], ['1', '€ 23477.04']],
                             widget=widgets.RadioSelectHorizontal,
                             label='2.In base alla figura mostrata quale sarà il vostro guadagno se la variazione sarà del  +12%',
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
