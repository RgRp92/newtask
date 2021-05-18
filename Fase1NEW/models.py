from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
)

author = 'RR'

doc = """
Beliefs Task
"""
# To read from the CSV file
import pandas as pd

class Constants(BaseConstants):
    name_in_url = 'Fase1NEW'
    num_rounds = 3
    players_per_group = None
    app_name = 'Fase1NEW'

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
    quiz = models.CharField(choices=[['0', '12.44'],['2', '14.94'],['1','13.69']],
                               widget= widgets.RadioSelectHorizontal,
                               label='1. In base alla figura mostrata quale sarà il vostro guadagno se il reddito varierà del + 2%',
                              blank=True,default = "")
    quiz2 = models.CharField(choices=[['0', '17.44'], ['1', '14.94'], ['2', '13.69']],
                               widget=widgets.RadioSelectHorizontal,
                               label='2.In base alla figura mostrata quale sarà il vostro guadagno se il reddito varierà del - 25%',
                              blank=True,default = "" )

    labelset = models.IntegerField(default = 0)

    final_payment = models.StringField()

    bin1  = models.IntegerField(initial = 0)
    bin2  = models.IntegerField(initial = 0)
    bin3  = models.IntegerField(initial = 0)
    bin4  = models.IntegerField(initial = 0)
    bin5  = models.IntegerField(initial = 0)
    bin6  = models.IntegerField(initial = 0)

    pref1 = models.IntegerField(default = 0, min=0, max=100, initial=0, label="")
    pref2 = models.IntegerField(default = 0, min=0, max=100, initial=0, label="")
    pref3 = models.IntegerField(default = 0, min=0, max=100, initial=0, label="")

    sum_token = models.FloatField(min=100, max=100)

    w_amt = models.FloatField(default=0,min=0,label="")
