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

    s1_a1 = [18622, 18422,18122,18022,17922,17897,17872,17842,17811,17782,17752,17722,17692]

    s1_a2 = [17091,16891,16591,16491,16391,16366,16341,16311,16280,16251,16221,16191,16161]

    s1_a3 = [19133,18933,18633,18533,18433,18408,18383,18353,18322,18293,18263,18233,18203]

    s1_a4 = [21174,20974,20674,20574,20474,20449,20424,20394,20363,20334,20304,20274,20244]

    s1_a5 = [23216,23016,22716,22616,22516,22491,22466,22436,22405,22376,22346,22316,22286]

    s1_a6 = [25257,25057,24757,24657,24557,24532,24507,24477,24446,24417,24387,24357,24327]

    diff_1 = [3311, 261]
    diff_2 = [3111, 461]
    diff_3 = [2811, 761]
    diff_4 = [2711, 861]
    diff_5 = [2611, 961]
    diff_6 = [2586, 986]
    diff_7 = [2561, 1011]
    diff_8 = [2531, 1041]
    diff_9 = [2500, 1072]
    diff_10 = [2471, 1101]
    diff_11 = [2441, 1131]
    diff_12 = [2411, 1161]
    diff_13 = [2381, 1191]

    s1_b1 = [15311,17353,19394,21436,23477,25519]



class Group(BaseGroup):
    pass

class Subsession(BaseSubsession):
    pass

class Player(BasePlayer):

    quiz = models.CharField(choices=[['1', '20574 €'], ['2', '18533 €'], ['2', '21436 €']],
                            widget=widgets.RadioSelectHorizontal,
                            label='In base alla figura mostrata, quale sarà il vostro guadagno se la variazione sarà del + 2%?',
                            blank=True, default="")

    quiz2 = models.CharField(choices=[['1', '20574 €'], ['2', '18533 €'], ['2', '21436 €']],
                             widget=widgets.RadioSelectHorizontal,
                             label='In base alla figura mostrata quale sarà il vostro guadagno se la variazione sarà del +2%?',
                             blank=True, default="")

    quiz3 = models.CharField(choices=[['2', '21436 €'], ['1', '19394 €'], ['2', '18383 €']],
                            widget=widgets.RadioSelectHorizontal,
                            label='In base alla figura mostrata quale sarà il vostro guadagno se la variazione sarà del - 8%?',
                            blank=True, default="")
    quiz4 = models.CharField(choices=[['2', '21436 €'], ['1', '19394 €'], ['2', '18383 €']],
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
    HL_11 = models.IntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal,initial=0)
    HL_12 = models.IntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal,initial=0)
    HL_13 = models.IntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal,initial=0)

    HL = models.IntegerField(choices=[[1,'A'],[2,'B']],widget=widgets.RadioSelectHorizontal,initial=0)



    # Define here the methods associated to Players
    # this method is needed to compute payoffs
    def set_payoff_HL(self):
        #*******************************************
        # select random row and random outcome
        #*******************************************
        #
        self.participant.vars['HL_row'] = random.randint(1,13)

        # select one row randomly for payment (from module random)
        self.participant.vars['HL_random'] = random.randint(1,13)

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
                   self.HL_11,self.HL_12,self.HL_13]


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
        elif self.participant.vars['HL_scenario'] > 30 and self.participant.vars['HL_scenario'] <= 53:
            # if the random number is larger than the random row
            if self.participant.vars['HL_choice_s1'] == 1 :#A
                    # if the choice was A
                self.participant.vars['payoff_HL'] = Constants.s1_a2[self.participant.vars['HL_row']-1]
                    # because HL_row is the same as p in the MPL
            else:
                self.participant.vars['payoff_HL'] = Constants.s1_b1[1]
        elif self.participant.vars['HL_scenario'] > 53 and self.participant.vars['HL_scenario'] <= 73:
            # if the random number is larger than the random row
            if self.participant.vars['HL_choice_s1'] == 1 :#A
                    # if the choice was A
                self.participant.vars['payoff_HL'] = Constants.s1_a3[self.participant.vars['HL_row']-1]
                    # because HL_row is the same as p in the MPL
            else:
                self.participant.vars['payoff_HL'] = Constants.s1_b1[2]
        elif self.participant.vars['HL_scenario'] > 73 and self.participant.vars['HL_scenario'] <= 85:
            # if the random number is larger than the random row
            if self.participant.vars['HL_choice_s1'] == 1 :#A
                    # if the choice was A
                self.participant.vars['payoff_HL'] = Constants.s1_a4[self.participant.vars['HL_row']-1]
                    # because HL_row is the same as p in the MPL
            else:
                self.participant.vars['payoff_HL'] = Constants.s1_b1[3]
        elif self.participant.vars['HL_scenario'] > 85 and self.participant.vars['HL_scenario'] <= 94:
            # if the random number is larger than the random row
            if self.participant.vars['HL_choice_s1'] == 1 :#A
                    # if the choice was A
                self.participant.vars['payoff_HL'] = Constants.s1_a5[self.participant.vars['HL_row']-1]
                    # because HL_row is the same as p in the MPL
            else:
                self.participant.vars['payoff_HL'] = Constants.s1_b1[4]
        elif self.participant.vars['HL_scenario'] > 94 and self.participant.vars['HL_scenario'] <= 100:
            # if the random number is larger than the random row
            if self.participant.vars['HL_choice_s1'] == 1 :#A
                    # if the choice was A
                self.participant.vars['payoff_HL'] = Constants.s1_a6[self.participant.vars['HL_row']-1]
                    # because HL_row is the same as p in the MPL
            else:
                self.participant.vars['payoff_HL'] = Constants.s1_b1[5]


        self.payoff = self.participant.vars['payoff_HL']
        # write the payoff to player.payoff
