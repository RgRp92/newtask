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

import random

author = 'Ruggiero Rippo'

doc = """
Random Draw for Final payment
"""


class Constants(BaseConstants):
    name_in_url = 'FinalPayment'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    def creating_session(self):
        num_participant = self.session.num_participants
        if num_participant <= 10:
            num_winners = 1
        else:  num_winners = int(0.1*num_participant)
        winners = random.sample(range(1,num_participant+1),num_winners)
        app = random.randint(1,3)
        self.session.vars["winners"] = winners
        self.session.vars["app"] = app
        self.session.vars["id"] = BasePlayer.id_in_group


class Group(BaseGroup):
    pass


class Player(BasePlayer):
  pass