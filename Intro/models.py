from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Ruggiero Rippo'

doc = """
Introduction to the experiment
"""


class Constants(BaseConstants):
    name_in_url = 'Intro'
    num_rounds = 1
    players_per_group = None
    app_name = 'Intro'


class Subsession(BaseSubsession):
    def creating_session(self):
        num_participant = self.session.num_participants
        if num_participant <= 10:
            num_winners = 1
        else:  num_winners = int(0.1*num_participant)

        self.session.vars["n_winners"] = num_winners


class Group(BaseGroup):
    pass


class Player(BasePlayer):
   pass