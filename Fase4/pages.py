from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Page0(Page):
    def is_displayed(self):
        return self.round_number == 1

class Page1Demographics(Page):
    form_model = 'player'
    form_fields = ['q1','q2','q3']

class Page2AgriAct(Page):
        form_model = 'player'
        form_fields = ['q4', 'q5', 'q6', 'q7',
                       'q8_a', 'q8_b', 'q8_c',
                       'q9_a', 'q9_b', 'q9_c', 'q9_d', 'q9_e','q9_f','q9_g','q9_h','q9_i','q9_j',
                       'q10_a1','q10_a2','q10_a3','q10_a4','q10_a5',
                       'q10_b1','q10_b2','q10_b3','q10_b4','q10_b5',
                       'q10_c1','q10_c2','q10_c3','q10_c4','q10_c5',
                       'q10_d1', 'q10_d2', 'q10_d3', 'q10_d4', 'q10_d5',
                       'q10_e1', 'q10_e2', 'q10_e3', 'q10_e4', 'q10_e5',
                       'q10_f1', 'q10_f2', 'q10_f3', 'q10_f4', 'q10_f5',
                       'q11',]

class Page3AgriAct2(Page):
    form_model = 'player'
    form_fields = ['q12','q13','q14','q15']

class Page4ISTsurvey(Page):
    form_model = 'player'
    form_fields = ['q16','q16_a','q16_b','q16_c','q16_d',
                   'q17','q18','q19','q20','q21']

class Page5LikertScaleQ(Page):
    form_model = 'player'
    form_fields = ['qc1','qc2','qc3','qc4',
                   'qt1','qt2','qt3','qt4','qt5']

class Page6LikertScaleQ1(Page):
    form_model = 'player'
    form_fields = ['qh1','qh2','qh3',
                   'qs1','qs2','qs3','qs4']

class ResultsWaitPage(WaitPage):
    pass

class Results(Page):
    form_model = 'player'

page_sequence = [Page0,
                 Page1Demographics,
                 Page2AgriAct,
                 Page3AgriAct2,
                 Page4ISTsurvey,
                 Page5LikertScaleQ,
                 Page6LikertScaleQ1,
                 Results]
