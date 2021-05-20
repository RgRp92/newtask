from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
)

author = 'RR'

doc = """
Beliefs Task
"""
# To read from the CSV file
import pandas as pd
import random

class Constants(BaseConstants):
    name_in_url = 'Fase1cda'
    num_rounds = 1
    players_per_group = None
    app_name = 'Fase1cda'

    # Colors picked with a good pallete
    hex_colors = ["#F8766D", "#00BFC4"]


class Subsession(BaseSubsession):
    def creating_session(self):

        farm_dat = pd.read_csv("farmdata/data.csv")
        self.session.vars["beliefs_farm_dat"] = farm_dat
        self.session.vars["beliefs_hex_colors"] = ["#ff9933", "#00BFC4"]

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    quizf1 = models.CharField(choices=[['0', '12.44'], ['2', '14.94'], ['1', '13.69']],
                              widget=widgets.RadioSelectHorizontal,
                              label='1. In base alla figura mostrata quale sarà il vostro guadagno se il reddito varierà del + 2%',
                              blank=True, default="")
    quiz2f1 = models.CharField(choices=[['0', '12.44'], ['2', '14.94'], ['1', '13.69']],
                               widget=widgets.RadioSelectHorizontal,
                               label='1. In base alla figura mostrata quale sarà il vostro guadagno se il reddito varierà del + 2%',
                               blank=True, default="")
    quiz3f1 = models.CharField(choices=[['0', '17.44'], ['1', '14.94'], ['2', '13.69']],
                               widget=widgets.RadioSelectHorizontal,
                               label='2.In base alla figura mostrata quale sarà il vostro guadagno se il reddito varierà del - 25%',
                               blank=True, default="")

    quiz4f1 = models.CharField(choices=[['0', '17.44'], ['1', '14.94'], ['2', '13.69']],
                               widget=widgets.RadioSelectHorizontal,
                               label='2.In base alla figura mostrata quale sarà il vostro guadagno se il reddito varierà del - 25%',
                               blank=True, default="")

    labelset = models.IntegerField(default=0)

    final_payment = models.StringField()

    bin1 = models.IntegerField(initial=0)
    bin2 = models.IntegerField(initial=0)
    bin3 = models.IntegerField(initial=0)
    bin4 = models.IntegerField(initial=0)
    bin5 = models.IntegerField(initial=0)
    bin6 = models.IntegerField(initial=0)



    w_amt = models.FloatField(default=0,min=0,label="")

    def set_winning_bin(self):
        self.participant.vars['variation'] = random.randint(1, 100)

        if self.participant.vars['variation'] <= 30:
            self.participant.vars['nw_bin'] = "1"
        elif self.participant.vars['variation'] > 30 and self.participant.vars['variation'] <= 53:
            self.participant.vars['nw_bin'] = "2"
        elif self.participant.vars['variation'] > 53 and self.participant.vars['variation']<= 73:
            self.participant.vars['nw_bin'] = "3"
        elif  self.participant.vars['variation'] > 73 and self.participant.vars['variation']<= 85:
            self.participant.vars['nw_bin'] = "4"
        elif self.participant.vars['variation'] > 85 and self.participant.vars['variation']<= 94:
            self.participant.vars['nw_bin'] = "5"
        else:
            self.participant.vars['nw_bin'] = "6"