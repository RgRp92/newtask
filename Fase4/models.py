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
Fase 4 Questionario
"""


class Constants(BaseConstants):
    name_in_url = 'Fase4'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    q1 = models.IntegerField(label='1. Anno di nascita', min=1900, max=2012)
    q2 = models.StringField(
        choices=[['1', 'M'], ['2', 'F']],
        label='2. Genere',
        widget=widgets.RadioSelect,
    )
    q3 = models.StringField(
        choices=[['1', 'Scuola elementare'], ['2', 'Diploma scuola superiore'],
                 ['3', 'Laurea 3 anni'], ['4', 'Laurea 5 anni'], ['5', 'Master'],
                 ['6', 'Dottorato']],
        label='3. Titolo di studio',
        widget=widgets.RadioSelect,
    )
    q4 = models.StringField(
        choices=[['1', 'Fino a 5 anni'], ['2', 'Da 5 a 9 anni'],
                 ['3', 'Da 10 a 20 anni'],
                 ['4', 'Più di 20 anni']],
        label='4. Da quanti anni è coinvolto nella coltivazione delle mele?',
        widget=widgets.RadioSelect,
    )
    q5 = models.FloatField(min=1,
                             label='5. A quanti ettari corrisponde la superfice agricola della sua azienda?'
                             )
    q6 = models.IntegerField(min=1, max=100,
                             label='6.	Quanti ettari in percentuale occupa la coltivazione a mele? (max 100%)'
                             )
    q7 = models.StringField(
        choices=[['1', 'Alta val di Non, Val di Sole'],
                 ['2', 'Bassa Val di non'],
                 ['3', 'Bleggio, Alto Garda, Ledro, Paganella'],
                 ['4', 'Valle dei Laghi'],
                 ['5', 'Piana Rotaliana'],
                 ['6', 'Valsugana'],
                 ['7', 'Territori dell Adige, Vallagarina, Valle di Cembra']],
        label='7. Zona di produzione',
        widget=widgets.RadioSelect,
    )
    q8_a = models.BooleanField(blank=True, initial=False)
    q8_b = models.BooleanField(blank=True, initial=False)
    q8_c = models.BooleanField(blank=True, initial=False)

    q9_a = models.BooleanField(blank=True, initial=False)
    q9_b = models.BooleanField(blank=True, initial=False)
    q9_c = models.BooleanField(blank=True, initial=False)
    q9_d = models.BooleanField(blank=True, initial=False)
    q9_e = models.BooleanField(blank=True, initial=False)
    q9_f = models.BooleanField(blank=True, initial=False)
    q9_g = models.BooleanField(blank=True, initial=False)
    q9_h = models.BooleanField(blank=True, initial=False)
    q9_i = models.BooleanField(blank=True, initial=False)
    q9_j = models.BooleanField(blank=True, initial=False)

    q10_a1 = models.BooleanField(blank=True, initial=False)
    q10_a2 = models.BooleanField(blank=True, initial=False)
    q10_a3 = models.BooleanField(blank=True, initial=False)
    q10_a4 = models.BooleanField(blank=True, initial=False)
    q10_a5 = models.BooleanField(blank=True, initial=False)

    q10_b1 = models.BooleanField(blank=True, initial=False)
    q10_b2 = models.BooleanField(blank=True, initial=False)
    q10_b3 = models.BooleanField(blank=True, initial=False)
    q10_b4 = models.BooleanField(blank=True, initial=False)
    q10_b5 = models.BooleanField(blank=True, initial=False)

    q10_c1 = models.BooleanField(blank=True, initial=False)
    q10_c2 = models.BooleanField(blank=True, initial=False)
    q10_c3 = models.BooleanField(blank=True, initial=False)
    q10_c4 = models.BooleanField(blank=True, initial=False)
    q10_c5 = models.BooleanField(blank=True, initial=False)

    q10_d1 = models.BooleanField(blank=True, initial=False)
    q10_d2 = models.BooleanField(blank=True, initial=False)
    q10_d3 = models.BooleanField(blank=True, initial=False)
    q10_d4 = models.BooleanField(blank=True, initial=False)
    q10_d5 = models.BooleanField(blank=True, initial=False)

    q10_e1 = models.BooleanField(blank=True, initial=False)
    q10_e2 = models.BooleanField(blank=True, initial=False)
    q10_e3 = models.BooleanField(blank=True, initial=False)
    q10_e4 = models.BooleanField(blank=True, initial=False)
    q10_e5 = models.BooleanField(blank=True, initial=False)

    q10_f1 = models.BooleanField(blank=True, initial=False)
    q10_f2 = models.BooleanField(blank=True, initial=False)
    q10_f3 = models.BooleanField(blank=True, initial=False)
    q10_f4 = models.BooleanField(blank=True, initial=False)
    q10_f5 = models.BooleanField(blank=True, initial=False)

    q11 = models.StringField(
        choices=[['1', 'SI'], ['2', 'NO']],
        label='11. Fa parte di una OP?',
        widget=widgets.RadioSelect)

    q12 = models.StringField(
        choices=[['1', 'Tra € 0 e € 24.999'],
                 ['2 ', 'Tra € 25.000 e € 49.999 '],
                 ['3', 'Tra € 50.000 e € 74.999'],
                 ['4', 'Tra € 75.000 e € 100.000'],
                 ['5', 'Oltre € 100.000']],
        label='12. Negli ultimi 3 anni quale è stato il suo reddito ad ettaro netto? ',
        widget=widgets.RadioSelect)


    q13 = models.IntegerField(label='13. Negli ultimi 3 anni, quale percentuale del suo reddito è derivata da mele? (max 100%)'
                                    '', min=0, max=100)

    q14 = models.IntegerField(label='14. Negli ultimi 3 anni, quanto hanno inciso i costi per la produzione di mele ad ettaro?(max 100%)'
                                    '', min=0, max=100)

    q15 = models.StringField(
        choices=[['1', 'SI'], ['2', 'NO'],['3','Non saprei']],
        label='15. Pensa che la sua attività melicola sarà continuata nel futuro da un familiare?',
        widget=widgets.RadioSelect)

    q16 = models.StringField(
        choices=[['1', 'SI'], ['2', 'NO']],
        label='16. Nel 2021 ha sottoscritto la partecipazione e la copertura mutualisitca Fondo IST-Mele?',
        widget=widgets.RadioSelect)

    q16_a = models.BooleanField(blank=True, initial=False)
    q16_b = models.BooleanField(blank=True, initial=False)
    q16_c = models.BooleanField(blank=True, initial=False)
    q16_d = models.BooleanField(blank=True, initial=False)

    q17 = models.StringField(
        choices=[['1','50 €/ettaro'],['2','100 €/ettaro'],['3','150 €/ettaro'],['4','200 €/ettaro'],['5','250 €/ettaro']],
        label= '17. Quanti €/ettaro preferisce pagare come quota fissa per aderire alla copertura '
               'mutualistica del Fondo IST mele?',
        widget=widgets.RadioSelect)

    q18 = models.StringField(
        choices=[['1', '10%'], ['2', '15%'],['3', '20%'],['4', '25%'],['5', '30%']],
        label='18. Quale soglia di reddito per il Fondo IST mele preferisce tra queste?',
        widget=widgets.RadioSelect)

    q19 = models.StringField(
        choices=[['1', 'Fino al 60%'], ['2', 'Fino al 65%'],['3', 'Fino al 70%'],['4', 'Fino al 75%'],['5', 'Fino al 80%']],
        label='19. Quale percentuale di compensazione dal Fondo IST Mele preferisce tra queste?',
        widget=widgets.RadioSelect)

    q20 = models.StringField(
        choices=[['1', 'Su base triennale'], ['2', 'Su base quinquennale']],
        label='20. Preferisce che il reddito medio venga calcolato:',
        widget=widgets.RadioSelect )

    q21 = models.StringField(
        choices=[['1', 'Dipendando dal Trigger Event'],
                 ['2','Non dipendano dal Trigger Event'],
                 ['3', 'Non saprei']],
        label='21. Preferisce che le richieste di risarcimento al Fondo IST Mele:',
        widget=widgets.RadioSelect )

    qc1 = models.StringField(
        choices=[['1',''], ['2',''],['3',''],['4',''],['5','']],
        label='Cooperazione',
        widget=widgets.RadioSelectHorizontal,
    )
    qc2 = models.StringField(
        choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', '']],
        label='Cooperazione',
        widget=widgets.RadioSelectHorizontal,
    )
    qc3 = models.StringField(
        choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', '']],
        label='Cooperazione',
        widget=widgets.RadioSelectHorizontal,
    )
    qc4 = models.StringField(
        choices=[['1',''], ['2',''],['3',''],['4',''],['5','']],
        label='Cooperazione',
        widget=widgets.RadioSelectHorizontal,
    )
    qt1 = models.StringField(
        choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', '']],
        label='Cooperazione',
        widget=widgets.RadioSelectHorizontal,
    )
    qt2 = models.StringField(
        choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', '']],
        label='Cooperazione',
        widget=widgets.RadioSelectHorizontal,
    )
    qt3 = models.StringField(
        choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', '']],
        label='Cooperazione',
        widget=widgets.RadioSelectHorizontal,
    )
    qt4 = models.StringField(
        choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', '']],
        label='Cooperazione',
        widget=widgets.RadioSelectHorizontal,
    )
    qt5 = models.StringField(
        choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', '']],
        label='Cooperazione',
        widget=widgets.RadioSelectHorizontal,
    )
    qh1 = models.StringField(
        choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', '']],
        label='Cooperazione',
        widget=widgets.RadioSelectHorizontal,
    )
    qh3 = models.StringField(
        choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', '']],
        label='Cooperazione',
        widget=widgets.RadioSelectHorizontal,
    )
    qh2 = models.StringField(
        choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', '']],
        label='Cooperazione',
        widget=widgets.RadioSelectHorizontal,
    )
    qs1 = models.StringField(
        choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', '']],
        label='Cooperazione',
        widget=widgets.RadioSelectHorizontal,
    )
    qs2 = models.StringField(
        choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', '']],
        label='Cooperazione',
        widget=widgets.RadioSelectHorizontal,
    )
    qs3 = models.StringField(
        choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', '']],
        label='Cooperazione',
        widget=widgets.RadioSelectHorizontal,
    )
    qs4 = models.StringField(
        choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', '']],
        label='Cooperazione',
        widget=widgets.RadioSelectHorizontal,
    )
