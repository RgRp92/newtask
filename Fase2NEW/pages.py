from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Page0(Page):

    def is_displayed(self):
        return self.round_number == 1

class ISTPage1(Page):
    form_model = 'player'

class ISTPage2(Page):
    form_model = 'player'

class ISTPage3(Page):
    form_model = 'player'

class ISTPage4(Page):
    form_model = 'player'

class IstruzioniPage1(Page):
    form_model = 'player'

class IstruzioniPage3bis(Page):
    form_model = 'player'
    def vars_for_template(self):
        # retrieve values from constants and store them in a dictionary
        var1 = Constants.var1 * 100
        var11 = Constants.var11 * 100
        var2 = Constants.var2 * 100
        var22 = Constants.var22 * 100
        var3 = Constants.var3 * 100
        var33 = Constants.var33 * 100
        var4 = Constants.var4 * 100
        var44 = Constants.var44 * 100
        var5 = Constants.var5 * 100
        var55 = Constants.var55 * 100


        return {
            'var1': var1,
            'var11': var11,
            'var2': var2,
            'var22': var22,
            'var3': var3,
            'var33': var33,
            'var4': var4,
            'var44': var44,
            'var5': var5,
            'var55': var55,

            'ist4': Constants.ist[3],
            's1_a1_4': Constants.s1_a1[3],
            's1_a2_4': Constants.s1_a2[3],
            's1_a3_4': Constants.s1_a3[3],
            's1_a4_4': Constants.s1_a4[3],
            's1_a5_4': Constants.s1_a5[3],

            's1_b1_1': Constants.s1_b1[0],
            's1_b1_2': Constants.s1_b1[1],
            's1_b1_3': Constants.s1_b1[2],
            's1_b1_4': Constants.s1_b1[3],
            's1_b1_5': Constants.s1_b1[4],

            'diff_a': Constants.diff_4[0],
            'diff_b': Constants.diff_4[1],

        }

class IstruzioniPage4(Page):
    form_model = 'player'

class IstruzioniPage5(Page):
    form_model = 'player'

class EsempioPage1(Page):
    def vars_for_template(self):
        # retrieve values from constants and store them in a dictionary
        var1 = Constants.var1 * 100
        var11 = Constants.var11 * 100
        var2 = Constants.var2 * 100
        var22 = Constants.var22 * 100
        var3 = Constants.var3 * 100
        var33 = Constants.var33 * 100
        var4 = Constants.var4 * 100
        var44 = Constants.var44 * 100
        var5 = Constants.var5 * 100
        var55 = Constants.var55 * 100


        return {
            'var1': var1,
            'var11': var11,
            'var2': var2,
            'var22': var22,
            'var3': var3,
            'var33': var33,
            'var4': var4,
            'var44': var44,
            'var5': var5,
            'var55': var55,

            'ist4': Constants.ist[3],
            's1_a1_4': Constants.s1_a1[3],
            's1_a2_4': Constants.s1_a2[3],
            's1_a3_4': Constants.s1_a3[3],
            's1_a4_4': Constants.s1_a4[3],
            's1_a5_4': Constants.s1_a5[3],

            's1_b1_1': Constants.s1_b1[0],
            's1_b1_2': Constants.s1_b1[1],
            's1_b1_3': Constants.s1_b1[2],
            's1_b1_4': Constants.s1_b1[3],
            's1_b1_5': Constants.s1_b1[4],

            'diff_a': Constants.diff_4[0],
            'diff_b': Constants.diff_4[1],

        }

class EsempioPage2(Page):
    def vars_for_template(self):
        # retrieve values from constants and store them in a dictionary
        var1 = Constants.var1 * 100
        var11 = Constants.var11 * 100
        var2 = Constants.var2 * 100
        var22 = Constants.var22 * 100
        var3 = Constants.var3 * 100
        var33 = Constants.var33 * 100
        var4 = Constants.var4 * 100
        var44 = Constants.var44 * 100
        var5 = Constants.var5 * 100
        var55 = Constants.var55 * 100


        return {
            'var1': var1,
            'var11': var11,
            'var2': var2,
            'var22': var22,
            'var3': var3,
            'var33': var33,
            'var4': var4,
            'var44': var44,
            'var5': var5,
            'var55': var55,

            'ist4': Constants.ist[3],
            's1_a1_4': Constants.s1_a1[3],
            's1_a2_4': Constants.s1_a2[3],
            's1_a3_4': Constants.s1_a3[3],
            's1_a4_4': Constants.s1_a4[3],
            's1_a5_4': Constants.s1_a5[3],

            's1_b1_1': Constants.s1_b1[0],
            's1_b1_2': Constants.s1_b1[1],
            's1_b1_3': Constants.s1_b1[2],
            's1_b1_4': Constants.s1_b1[3],
            's1_b1_5': Constants.s1_b1[4],

            'diff_a': Constants.diff_4[0],
            'diff_b': Constants.diff_4[1],

        }

class EsempioPage3(Page):
    def vars_for_template(self):
        # retrieve values from constants and store them in a dictionary
        var1 = Constants.var1 * 100
        var11 = Constants.var11 * 100
        var2 = Constants.var2 * 100
        var22 = Constants.var22 * 100
        var3 = Constants.var3 * 100
        var33 = Constants.var33 * 100
        var4 = Constants.var4 * 100
        var44 = Constants.var44 * 100
        var5 = Constants.var5 * 100
        var55 = Constants.var55 * 100



        return {
            'var1': var1,
            'var11': var11,
            'var2': var2,
            'var22': var22,
            'var3': var3,
            'var33': var33,
            'var4': var4,
            'var44': var44,
            'var5': var5,
            'var55': var55,

            'ist1': Constants.ist[0],
            'ist2': Constants.ist[1],
            'ist3': Constants.ist[2],
            'ist4': Constants.ist[3],
            'ist5': Constants.ist[4],
            'ist6': Constants.ist[5],
            'ist7': Constants.ist[6],
            'ist8': Constants.ist[7],
            'ist9': Constants.ist[8],
            'ist10': Constants.ist[9],
            'ist11': Constants.ist[10],
            'ist12': Constants.ist[11],


            's1_a1_1': Constants.s1_a1[0],
            's1_a1_2': Constants.s1_a1[1],
            's1_a1_3': Constants.s1_a1[2],
            's1_a1_4': Constants.s1_a1[3],
            's1_a1_5': Constants.s1_a1[4],
            's1_a1_6': Constants.s1_a1[5],
            's1_a1_7': Constants.s1_a1[6],
            's1_a1_8': Constants.s1_a1[7],
            's1_a1_9': Constants.s1_a1[8],
            's1_a1_10': Constants.s1_a1[9],
            's1_a1_11': Constants.s1_a1[10],
            's1_a1_12': Constants.s1_a1[11],

            's1_a2_1': Constants.s1_a2[0],
            's1_a2_2': Constants.s1_a2[1],
            's1_a2_3': Constants.s1_a2[2],
            's1_a2_4': Constants.s1_a2[3],
            's1_a2_5': Constants.s1_a2[4],
            's1_a2_6': Constants.s1_a2[5],
            's1_a2_7': Constants.s1_a2[6],
            's1_a2_8': Constants.s1_a2[7],
            's1_a2_9': Constants.s1_a2[8],
            's1_a2_10': Constants.s1_a2[9],
            's1_a2_11': Constants.s1_a2[10],
            's1_a2_12': Constants.s1_a2[11],


            's1_a3_1': Constants.s1_a3[0],
            's1_a3_2': Constants.s1_a3[1],
            's1_a3_3': Constants.s1_a3[2],
            's1_a3_4': Constants.s1_a3[3],
            's1_a3_5': Constants.s1_a3[4],
            's1_a3_6': Constants.s1_a3[5],
            's1_a3_7': Constants.s1_a3[6],
            's1_a3_8': Constants.s1_a3[7],
            's1_a3_9': Constants.s1_a3[8],
            's1_a3_10': Constants.s1_a3[9],
            's1_a3_11': Constants.s1_a3[10],
            's1_a3_12': Constants.s1_a3[11],


            's1_a4_1': Constants.s1_a4[0],
            's1_a4_2': Constants.s1_a4[1],
            's1_a4_3': Constants.s1_a4[2],
            's1_a4_4': Constants.s1_a4[3],
            's1_a4_5': Constants.s1_a4[4],
            's1_a4_6': Constants.s1_a4[5],
            's1_a4_7': Constants.s1_a4[6],
            's1_a4_8': Constants.s1_a4[7],
            's1_a4_9': Constants.s1_a4[8],
            's1_a4_10': Constants.s1_a4[9],
            's1_a4_11': Constants.s1_a4[10],
            's1_a4_12': Constants.s1_a4[11],


            's1_a5_1': Constants.s1_a5[0],
            's1_a5_2': Constants.s1_a5[1],
            's1_a5_3': Constants.s1_a5[2],
            's1_a5_4': Constants.s1_a5[3],
            's1_a5_5': Constants.s1_a5[4],
            's1_a5_6': Constants.s1_a5[5],
            's1_a5_7': Constants.s1_a5[6],
            's1_a5_8': Constants.s1_a5[7],
            's1_a5_9': Constants.s1_a5[8],
            's1_a5_10': Constants.s1_a5[9],
            's1_a5_12': Constants.s1_a5[10],
            's1_a5_11': Constants.s1_a5[11],


            's1_b1_1': Constants.s1_b1[0],
            's1_b1_2': Constants.s1_b1[1],
            's1_b1_3': Constants.s1_b1[2],
            's1_b1_4': Constants.s1_b1[3],
            's1_b1_5': Constants.s1_b1[4],

            'diff_a1': Constants.diff_1[0],
            'diff_b1': Constants.diff_1[1],
            'diff_a2': Constants.diff_2[0],
            'diff_b2': Constants.diff_2[1],
            'diff_a3': Constants.diff_3[0],
            'diff_b3': Constants.diff_3[1],
            'diff_a4': Constants.diff_4[0],
            'diff_b4': Constants.diff_4[1],
            'diff_a5': Constants.diff_5[0],
            'diff_b5': Constants.diff_5[1],
            'diff_a6': Constants.diff_6[0],
            'diff_b6': Constants.diff_6[1],
            'diff_a7': Constants.diff_7[0],
            'diff_b7': Constants.diff_7[1],
            'diff_a8': Constants.diff_8[0],
            'diff_b8': Constants.diff_8[1],
            'diff_a9': Constants.diff_9[0],
            'diff_b9': Constants.diff_9[1],
            'diff_a10': Constants.diff_10[0],
            'diff_b10': Constants.diff_10[1],
            'diff_a11': Constants.diff_11[0],
            'diff_b11': Constants.diff_11[1],
            'diff_a12': Constants.diff_12[0],
            'diff_b12': Constants.diff_12[1],

        }

class EsempioPage4(Page):
    def vars_for_template(self):
        # retrieve values from constants and store them in a dictionary
        var1 = Constants.var1 * 100
        var11 = Constants.var11 * 100
        var2 = Constants.var2 * 100
        var22 = Constants.var22 * 100
        var3 = Constants.var3 * 100
        var33 = Constants.var33 * 100
        var4 = Constants.var4 * 100
        var44 = Constants.var44 * 100
        var5 = Constants.var5 * 100
        var55 = Constants.var55 * 100



        return {
            'var1': var1,
            'var11': var11,
            'var2': var2,
            'var22': var22,
            'var3': var3,
            'var33': var33,
            'var4': var4,
            'var44': var44,
            'var5': var5,
            'var55': var55,

            'ist1': Constants.ist[0],
            'ist2': Constants.ist[1],
            'ist3': Constants.ist[2],
            'ist4': Constants.ist[3],
            'ist5': Constants.ist[4],
            'ist6': Constants.ist[5],
            'ist7': Constants.ist[6],
            'ist8': Constants.ist[7],
            'ist9': Constants.ist[8],
            'ist10': Constants.ist[9],
            'ist11': Constants.ist[10],
            'ist12': Constants.ist[11],


            's1_a1_1': Constants.s1_a1[0],
            's1_a1_2': Constants.s1_a1[1],
            's1_a1_3': Constants.s1_a1[2],
            's1_a1_4': Constants.s1_a1[3],
            's1_a1_5': Constants.s1_a1[4],
            's1_a1_6': Constants.s1_a1[5],
            's1_a1_7': Constants.s1_a1[6],
            's1_a1_8': Constants.s1_a1[7],
            's1_a1_9': Constants.s1_a1[8],
            's1_a1_10': Constants.s1_a1[9],
            's1_a1_11': Constants.s1_a1[10],
            's1_a1_12': Constants.s1_a1[11],

            's1_a2_1': Constants.s1_a2[0],
            's1_a2_2': Constants.s1_a2[1],
            's1_a2_3': Constants.s1_a2[2],
            's1_a2_4': Constants.s1_a2[3],
            's1_a2_5': Constants.s1_a2[4],
            's1_a2_6': Constants.s1_a2[5],
            's1_a2_7': Constants.s1_a2[6],
            's1_a2_8': Constants.s1_a2[7],
            's1_a2_9': Constants.s1_a2[8],
            's1_a2_10': Constants.s1_a2[9],
            's1_a2_11': Constants.s1_a2[10],
            's1_a2_12': Constants.s1_a2[11],


            's1_a3_1': Constants.s1_a3[0],
            's1_a3_2': Constants.s1_a3[1],
            's1_a3_3': Constants.s1_a3[2],
            's1_a3_4': Constants.s1_a3[3],
            's1_a3_5': Constants.s1_a3[4],
            's1_a3_6': Constants.s1_a3[5],
            's1_a3_7': Constants.s1_a3[6],
            's1_a3_8': Constants.s1_a3[7],
            's1_a3_9': Constants.s1_a3[8],
            's1_a3_10': Constants.s1_a3[9],
            's1_a3_11': Constants.s1_a3[10],
            's1_a3_12': Constants.s1_a3[11],


            's1_a4_1': Constants.s1_a4[0],
            's1_a4_2': Constants.s1_a4[1],
            's1_a4_3': Constants.s1_a4[2],
            's1_a4_4': Constants.s1_a4[3],
            's1_a4_5': Constants.s1_a4[4],
            's1_a4_6': Constants.s1_a4[5],
            's1_a4_7': Constants.s1_a4[6],
            's1_a4_8': Constants.s1_a4[7],
            's1_a4_9': Constants.s1_a4[8],
            's1_a4_10': Constants.s1_a4[9],
            's1_a4_11': Constants.s1_a4[10],
            's1_a4_12': Constants.s1_a4[11],


            's1_a5_1': Constants.s1_a5[0],
            's1_a5_2': Constants.s1_a5[1],
            's1_a5_3': Constants.s1_a5[2],
            's1_a5_4': Constants.s1_a5[3],
            's1_a5_5': Constants.s1_a5[4],
            's1_a5_6': Constants.s1_a5[5],
            's1_a5_7': Constants.s1_a5[6],
            's1_a5_8': Constants.s1_a5[7],
            's1_a5_9': Constants.s1_a5[8],
            's1_a5_10': Constants.s1_a5[9],
            's1_a5_12': Constants.s1_a5[10],
            's1_a5_11': Constants.s1_a5[11],


            's1_b1_1': Constants.s1_b1[0],
            's1_b1_2': Constants.s1_b1[1],
            's1_b1_3': Constants.s1_b1[2],
            's1_b1_4': Constants.s1_b1[3],
            's1_b1_5': Constants.s1_b1[4],

            'diff_a1': Constants.diff_1[0],
            'diff_b1': Constants.diff_1[1],
            'diff_a2': Constants.diff_2[0],
            'diff_b2': Constants.diff_2[1],
            'diff_a3': Constants.diff_3[0],
            'diff_b3': Constants.diff_3[1],
            'diff_a4': Constants.diff_4[0],
            'diff_b4': Constants.diff_4[1],
            'diff_a5': Constants.diff_5[0],
            'diff_b5': Constants.diff_5[1],
            'diff_a6': Constants.diff_6[0],
            'diff_b6': Constants.diff_6[1],
            'diff_a7': Constants.diff_7[0],
            'diff_b7': Constants.diff_7[1],
            'diff_a8': Constants.diff_8[0],
            'diff_b8': Constants.diff_8[1],
            'diff_a9': Constants.diff_9[0],
            'diff_b9': Constants.diff_9[1],
            'diff_a10': Constants.diff_10[0],
            'diff_b10': Constants.diff_10[1],
            'diff_a11': Constants.diff_11[0],
            'diff_b11': Constants.diff_11[1],
            'diff_a12': Constants.diff_12[0],
            'diff_b12': Constants.diff_12[1],

        }

class EsempioPage5(Page):
    def vars_for_template(self):
        # retrieve values from constants and store them in a dictionary
        var1 = Constants.var1 * 100
        var11 = Constants.var11 * 100
        var2 = Constants.var2 * 100
        var22 = Constants.var22 * 100
        var3 = Constants.var3 * 100
        var33 = Constants.var33 * 100
        var4 = Constants.var4 * 100
        var44 = Constants.var44 * 100
        var5 = Constants.var5 * 100
        var55 = Constants.var55 * 100



        return {
            'var1': var1,
            'var11': var11,
            'var2': var2,
            'var22': var22,
            'var3': var3,
            'var33': var33,
            'var4': var4,
            'var44': var44,
            'var5': var5,
            'var55': var55,

            'ist1': Constants.ist[0],
            'ist2': Constants.ist[1],
            'ist3': Constants.ist[2],
            'ist4': Constants.ist[3],
            'ist5': Constants.ist[4],
            'ist6': Constants.ist[5],
            'ist7': Constants.ist[6],
            'ist8': Constants.ist[7],
            'ist9': Constants.ist[8],
            'ist10': Constants.ist[9],
            'ist11': Constants.ist[10],
            'ist12': Constants.ist[11],


            's1_a1_1': Constants.s1_a1[0],
            's1_a1_2': Constants.s1_a1[1],
            's1_a1_3': Constants.s1_a1[2],
            's1_a1_4': Constants.s1_a1[3],
            's1_a1_5': Constants.s1_a1[4],
            's1_a1_6': Constants.s1_a1[5],
            's1_a1_7': Constants.s1_a1[6],
            's1_a1_8': Constants.s1_a1[7],
            's1_a1_9': Constants.s1_a1[8],
            's1_a1_10': Constants.s1_a1[9],
            's1_a1_11': Constants.s1_a1[10],
            's1_a1_12': Constants.s1_a1[11],

            's1_a2_1': Constants.s1_a2[0],
            's1_a2_2': Constants.s1_a2[1],
            's1_a2_3': Constants.s1_a2[2],
            's1_a2_4': Constants.s1_a2[3],
            's1_a2_5': Constants.s1_a2[4],
            's1_a2_6': Constants.s1_a2[5],
            's1_a2_7': Constants.s1_a2[6],
            's1_a2_8': Constants.s1_a2[7],
            's1_a2_9': Constants.s1_a2[8],
            's1_a2_10': Constants.s1_a2[9],
            's1_a2_11': Constants.s1_a2[10],
            's1_a2_12': Constants.s1_a2[11],


            's1_a3_1': Constants.s1_a3[0],
            's1_a3_2': Constants.s1_a3[1],
            's1_a3_3': Constants.s1_a3[2],
            's1_a3_4': Constants.s1_a3[3],
            's1_a3_5': Constants.s1_a3[4],
            's1_a3_6': Constants.s1_a3[5],
            's1_a3_7': Constants.s1_a3[6],
            's1_a3_8': Constants.s1_a3[7],
            's1_a3_9': Constants.s1_a3[8],
            's1_a3_10': Constants.s1_a3[9],
            's1_a3_11': Constants.s1_a3[10],
            's1_a3_12': Constants.s1_a3[11],


            's1_a4_1': Constants.s1_a4[0],
            's1_a4_2': Constants.s1_a4[1],
            's1_a4_3': Constants.s1_a4[2],
            's1_a4_4': Constants.s1_a4[3],
            's1_a4_5': Constants.s1_a4[4],
            's1_a4_6': Constants.s1_a4[5],
            's1_a4_7': Constants.s1_a4[6],
            's1_a4_8': Constants.s1_a4[7],
            's1_a4_9': Constants.s1_a4[8],
            's1_a4_10': Constants.s1_a4[9],
            's1_a4_11': Constants.s1_a4[10],
            's1_a4_12': Constants.s1_a4[11],


            's1_a5_1': Constants.s1_a5[0],
            's1_a5_2': Constants.s1_a5[1],
            's1_a5_3': Constants.s1_a5[2],
            's1_a5_4': Constants.s1_a5[3],
            's1_a5_5': Constants.s1_a5[4],
            's1_a5_6': Constants.s1_a5[5],
            's1_a5_7': Constants.s1_a5[6],
            's1_a5_8': Constants.s1_a5[7],
            's1_a5_9': Constants.s1_a5[8],
            's1_a5_10': Constants.s1_a5[9],
            's1_a5_12': Constants.s1_a5[10],
            's1_a5_11': Constants.s1_a5[11],


            's1_b1_1': Constants.s1_b1[0],
            's1_b1_2': Constants.s1_b1[1],
            's1_b1_3': Constants.s1_b1[2],
            's1_b1_4': Constants.s1_b1[3],
            's1_b1_5': Constants.s1_b1[4],

            'diff_a1': Constants.diff_1[0],
            'diff_b1': Constants.diff_1[1],
            'diff_a2': Constants.diff_2[0],
            'diff_b2': Constants.diff_2[1],
            'diff_a3': Constants.diff_3[0],
            'diff_b3': Constants.diff_3[1],
            'diff_a4': Constants.diff_4[0],
            'diff_b4': Constants.diff_4[1],
            'diff_a5': Constants.diff_5[0],
            'diff_b5': Constants.diff_5[1],
            'diff_a6': Constants.diff_6[0],
            'diff_b6': Constants.diff_6[1],
            'diff_a7': Constants.diff_7[0],
            'diff_b7': Constants.diff_7[1],
            'diff_a8': Constants.diff_8[0],
            'diff_b8': Constants.diff_8[1],
            'diff_a9': Constants.diff_9[0],
            'diff_b9': Constants.diff_9[1],
            'diff_a10': Constants.diff_10[0],
            'diff_b10': Constants.diff_10[1],
            'diff_a11': Constants.diff_11[0],
            'diff_b11': Constants.diff_11[1],
            'diff_a12': Constants.diff_12[0],
            'diff_b12': Constants.diff_12[1],

        }

class Esperti(Page):
    form_model = 'player'

class Quiz1(Page):
    form_model = 'player'
    form_fields = ['quiz']

    def vars_for_template(self):
        # retrieve values from constants and store them in a dictionary
        var1 = Constants.var1 * 100
        var11 = Constants.var11 * 100
        var2 = Constants.var2 * 100
        var22 = Constants.var22 * 100
        var3 = Constants.var3 * 100
        var33 = Constants.var33 * 100
        var4 = Constants.var4 * 100
        var44 = Constants.var44 * 100
        var5 = Constants.var5 * 100
        var55 = Constants.var55 * 100

        return {
            'var1': var1,
            'var11': var11,
            'var2': var2,
            'var22': var22,
            'var3': var3,
            'var33': var33,
            'var4': var4,
            'var44': var44,
            'var5': var5,
            'var55': var55,

            'ist4': Constants.ist[3],
            's1_a1_4': Constants.s1_a1[3],
            's1_a2_4': Constants.s1_a2[3],
            's1_a3_4': Constants.s1_a3[3],
            's1_a4_4': Constants.s1_a4[3],
            's1_a5_4': Constants.s1_a5[3],

            's1_b1_1': Constants.s1_b1[0],
            's1_b1_2': Constants.s1_b1[1],
            's1_b1_3': Constants.s1_b1[2],
            's1_b1_4': Constants.s1_b1[3],
            's1_b1_5': Constants.s1_b1[4],

            'diff_a': Constants.diff_4[0],
            'diff_b': Constants.diff_4[1],
        }

    def before_next_page(self):
        self.participant.vars['quiz'] = self.player.quiz

class Quiz1Right(Page):
    form_model = 'player'

    def vars_for_template(self):
        # retrieve values from constants and store them in a dictionary
        var1 = Constants.var1 * 100
        var11 = Constants.var11 * 100
        var2 = Constants.var2 * 100
        var22 = Constants.var22 * 100
        var3 = Constants.var3 * 100
        var33 = Constants.var33 * 100
        var4 = Constants.var4 * 100
        var44 = Constants.var44 * 100
        var5 = Constants.var5 * 100
        var55 = Constants.var55 * 100

        return {
            'var1': var1,
            'var11': var11,
            'var2': var2,
            'var22': var22,
            'var3': var3,
            'var33': var33,
            'var4': var4,
            'var44': var44,
            'var5': var5,
            'var55': var55,

            'ist4': Constants.ist[3],
            's1_a1_4': Constants.s1_a1[3],
            's1_a2_4': Constants.s1_a2[3],
            's1_a3_4': Constants.s1_a3[3],
            's1_a4_4': Constants.s1_a4[3],
            's1_a5_4': Constants.s1_a5[3],

            's1_b1_1': Constants.s1_b1[0],
            's1_b1_2': Constants.s1_b1[1],
            's1_b1_3': Constants.s1_b1[2],
            's1_b1_4': Constants.s1_b1[3],
            's1_b1_5': Constants.s1_b1[4],

            'diff_a': Constants.diff_4[0],
            'diff_b': Constants.diff_4[1],
        }

    def is_displayed(self):
       return self.participant.vars["quiz"] == '1'

class Quiz2(Page):
    form_model = 'player'
    form_fields = ['quiz2']

    def vars_for_template(self):
        # retrieve values from constants and store them in a dictionary
        var1 = Constants.var1 * 100
        var11 = Constants.var11 * 100
        var2 = Constants.var2 * 100
        var22 = Constants.var22 * 100
        var3 = Constants.var3 * 100
        var33 = Constants.var33 * 100
        var4 = Constants.var4 * 100
        var44 = Constants.var44 * 100
        var5 = Constants.var5 * 100
        var55 = Constants.var55 * 100

        return {
            'var1': var1,
            'var11': var11,
            'var2': var2,
            'var22': var22,
            'var3': var3,
            'var33': var33,
            'var4': var4,
            'var44': var44,
            'var5': var5,
            'var55': var55,

            'ist4': Constants.ist[3],
            's1_a1_4': Constants.s1_a1[3],
            's1_a2_4': Constants.s1_a2[3],
            's1_a3_4': Constants.s1_a3[3],
            's1_a4_4': Constants.s1_a4[3],
            's1_a5_4': Constants.s1_a5[3],
            's1_b1_1': Constants.s1_b1[0],
            's1_b1_2': Constants.s1_b1[1],
            's1_b1_3': Constants.s1_b1[2],
            's1_b1_4': Constants.s1_b1[3],
            's1_b1_5': Constants.s1_b1[4],

            'diff_a': Constants.diff_4[0],
            'diff_b': Constants.diff_4[1],
        }

    def is_displayed(self):
       return self.participant.vars["quiz"] != '1'

    def before_next_page(self):
        self.participant.vars["quiz2"] = self.player.quiz2

class Quiz2Right(Page):
    form_model = 'player'


    def vars_for_template(self):

        # retrieve values from constants and store them in a dictionary
        var1 = Constants.var1 * 100
        var11 = Constants.var11 * 100
        var2 = Constants.var2 * 100
        var22 = Constants.var22 * 100
        var3 = Constants.var3 * 100
        var33 = Constants.var33 * 100
        var4 = Constants.var4 * 100
        var44 = Constants.var44 * 100
        var5 = Constants.var5 * 100
        var55 = Constants.var55 * 100

        return {
            'var1': var1,
            'var11': var11,
            'var2': var2,
            'var22': var22,
            'var3': var3,
            'var33': var33,
            'var4': var4,
            'var44': var44,
            'var5': var5,
            'var55': var55,

            'ist4': Constants.ist[3],
            's1_a1_4': Constants.s1_a1[3],
            's1_a2_4': Constants.s1_a2[3],
            's1_a3_4': Constants.s1_a3[3],
            's1_a4_4': Constants.s1_a4[3],
            's1_a5_4': Constants.s1_a5[3],

            's1_b1_1': Constants.s1_b1[0],
            's1_b1_2': Constants.s1_b1[1],
            's1_b1_3': Constants.s1_b1[2],
            's1_b1_4': Constants.s1_b1[3],
            's1_b1_5': Constants.s1_b1[4],

            'diff_a': Constants.diff_4[0],
            'diff_b': Constants.diff_4[1],
        }


    def is_displayed(self):
       return self.participant.vars["quiz"] !='1' and self.participant.vars["quiz2"] == '1'

class Quiz2bis(Page):
    form_model = 'player'


    def vars_for_template(self):

        # retrieve values from constants and store them in a dictionary
        var1 = Constants.var1 * 100
        var11 = Constants.var11 * 100
        var2 = Constants.var2 * 100
        var22 = Constants.var22 * 100
        var3 = Constants.var3 * 100
        var33 = Constants.var33 * 100
        var4 = Constants.var4 * 100
        var44 = Constants.var44 * 100
        var5 = Constants.var5 * 100
        var55 = Constants.var55 * 100

        return {
            'var1': var1,
            'var11': var11,
            'var2': var2,
            'var22': var22,
            'var3': var3,
            'var33': var33,
            'var4': var4,
            'var44': var44,
            'var5': var5,
            'var55': var55,

            'ist4': Constants.ist[3],
            's1_a1_4': Constants.s1_a1[3],
            's1_a2_4': Constants.s1_a2[3],
            's1_a3_4': Constants.s1_a3[3],
            's1_a4_4': Constants.s1_a4[3],
            's1_a5_4': Constants.s1_a5[3],

            's1_b1_1': Constants.s1_b1[0],
            's1_b1_2': Constants.s1_b1[1],
            's1_b1_3': Constants.s1_b1[2],
            's1_b1_4': Constants.s1_b1[3],
            's1_b1_5': Constants.s1_b1[4],

            'diff_a': Constants.diff_4[0],
            'diff_b': Constants.diff_4[1],
        }


    def is_displayed(self):
       return self.participant.vars["quiz"] !='1' and self.participant.vars["quiz2"] != '1'

class MyWaitPage(Page):
    form_model = 'player'

class HL_Page1(Page):
    # which forms are needed from class player
    form_model = 'player'
    form_fields = ['HL_1', 'HL_2', 'HL_3', 'HL_4', 'HL_5', 'HL_6', 'HL_7','HL_8','HL_9','HL_10','HL_11','HL_12'] # all 10 options

    # values that are to be displayed (dictionary)
    def vars_for_template(self):
        # retrieve values from constants and store them in a dictionary
        var1 = Constants.var1 * 100
        var11 = Constants.var11 * 100
        var2 = Constants.var2 * 100
        var22 = Constants.var22 * 100
        var3 = Constants.var3 * 100
        var33 = Constants.var33 * 100
        var4 = Constants.var4 * 100
        var44 = Constants.var44 * 100
        var5 = Constants.var5 * 100
        var55 = Constants.var55 * 100

        return {
            'var1': var1,
            'var11': var11,
            'var2': var2,
            'var22': var22,
            'var3': var3,
            'var33': var33,
            'var4': var4,
            'var44': var44,
            'var5': var5,
            'var55': var55,

            'ist1': Constants.ist[0],
            'ist2': Constants.ist[1],
            'ist3': Constants.ist[2],
            'ist4': Constants.ist[3],
            'ist5': Constants.ist[4],
            'ist6': Constants.ist[5],
            'ist7': Constants.ist[6],
            'ist8': Constants.ist[7],
            'ist9': Constants.ist[8],
            'ist10': Constants.ist[9],
            'ist11': Constants.ist[10],
            'ist12': Constants.ist[11],


            's1_a1_1': Constants.s1_a1[0],
            's1_a1_2': Constants.s1_a1[1],
            's1_a1_3': Constants.s1_a1[2],
            's1_a1_4': Constants.s1_a1[3],
            's1_a1_5': Constants.s1_a1[4],
            's1_a1_6': Constants.s1_a1[5],
            's1_a1_7': Constants.s1_a1[6],
            's1_a1_8': Constants.s1_a1[7],
            's1_a1_9': Constants.s1_a1[8],
            's1_a1_10': Constants.s1_a1[9],
            's1_a1_11': Constants.s1_a1[10],
            's1_a1_12': Constants.s1_a1[11],

            's1_a2_1': Constants.s1_a2[0],
            's1_a2_2': Constants.s1_a2[1],
            's1_a2_3': Constants.s1_a2[2],
            's1_a2_4': Constants.s1_a2[3],
            's1_a2_5': Constants.s1_a2[4],
            's1_a2_6': Constants.s1_a2[5],
            's1_a2_7': Constants.s1_a2[6],
            's1_a2_8': Constants.s1_a2[7],
            's1_a2_9': Constants.s1_a2[8],
            's1_a2_10': Constants.s1_a2[9],
            's1_a2_11': Constants.s1_a2[10],
            's1_a2_12': Constants.s1_a2[11],

            's1_a3_1': Constants.s1_a3[0],
            's1_a3_2': Constants.s1_a3[1],
            's1_a3_3': Constants.s1_a3[2],
            's1_a3_4': Constants.s1_a3[3],
            's1_a3_5': Constants.s1_a3[4],
            's1_a3_6': Constants.s1_a3[5],
            's1_a3_7': Constants.s1_a3[6],
            's1_a3_8': Constants.s1_a3[7],
            's1_a3_9': Constants.s1_a3[8],
            's1_a3_10': Constants.s1_a3[9],
            's1_a3_11': Constants.s1_a3[10],
            's1_a3_12': Constants.s1_a3[11],

            's1_a4_1': Constants.s1_a4[0],
            's1_a4_2': Constants.s1_a4[1],
            's1_a4_3': Constants.s1_a4[2],
            's1_a4_4': Constants.s1_a4[3],
            's1_a4_5': Constants.s1_a4[4],
            's1_a4_6': Constants.s1_a4[5],
            's1_a4_7': Constants.s1_a4[6],
            's1_a4_8': Constants.s1_a4[7],
            's1_a4_9': Constants.s1_a4[8],
            's1_a4_10': Constants.s1_a4[9],
            's1_a4_11': Constants.s1_a4[10],
            's1_a4_12': Constants.s1_a4[11],

            's1_a5_1': Constants.s1_a5[0],
            's1_a5_2': Constants.s1_a5[1],
            's1_a5_3': Constants.s1_a5[2],
            's1_a5_4': Constants.s1_a5[3],
            's1_a5_5': Constants.s1_a5[4],
            's1_a5_6': Constants.s1_a5[5],
            's1_a5_7': Constants.s1_a5[6],
            's1_a5_8': Constants.s1_a5[7],
            's1_a5_9': Constants.s1_a5[8],
            's1_a5_10': Constants.s1_a5[9],
            's1_a5_12': Constants.s1_a5[10],
            's1_a5_11': Constants.s1_a5[11],






            's1_b1_1': Constants.s1_b1[0],
            's1_b1_2': Constants.s1_b1[1],
            's1_b1_3': Constants.s1_b1[2],
            's1_b1_4': Constants.s1_b1[3],
            's1_b1_5': Constants.s1_b1[4],

            'diff_a1': Constants.diff_1[0],
            'diff_b1': Constants.diff_1[1],
            'diff_a2': Constants.diff_2[0],
            'diff_b2': Constants.diff_2[1],
            'diff_a3': Constants.diff_3[0],
            'diff_b3': Constants.diff_3[1],
            'diff_a4': Constants.diff_4[0],
            'diff_b4': Constants.diff_4[1],
            'diff_a5': Constants.diff_5[0],
            'diff_b5': Constants.diff_5[1],
            'diff_a6': Constants.diff_6[0],
            'diff_b6': Constants.diff_6[1],
            'diff_a7': Constants.diff_7[0],
            'diff_b7': Constants.diff_7[1],
            'diff_a8': Constants.diff_8[0],
            'diff_b8': Constants.diff_8[1],
            'diff_a9': Constants.diff_9[0],
            'diff_b9': Constants.diff_9[1],
            'diff_a10': Constants.diff_10[0],
            'diff_b10': Constants.diff_10[1],
            'diff_a11': Constants.diff_11[0],
            'diff_b11': Constants.diff_11[1],
            'diff_a12': Constants.diff_12[0],
            'diff_b12': Constants.diff_12[1],
        }


    # before moving to next page, compute payoffs (avoids that with refreshing payoffs are recomputed again)
    def before_next_page(self):
        # built-in method
        self.player.set_payoff_HL()# see in models in Player class
        self.participant.vars['a1_value'] = Constants.s1_a1[self.participant.vars['HL_row'] - 1]
        self.participant.vars['a2_value'] = Constants.s1_a2[self.participant.vars['HL_row'] - 1]
        self.participant.vars['a3_value'] = Constants.s1_a3[self.participant.vars['HL_row'] - 1]
        self.participant.vars['a4_value'] = Constants.s1_a4[self.participant.vars['HL_row'] - 1]
        self.participant.vars['a5_value'] = Constants.s1_a5[self.participant.vars['HL_row'] - 1]

        self.participant.vars['b1_value'] = Constants.s1_b1[0]
        self.participant.vars['b2_value'] = Constants.s1_b1[1]
        self.participant.vars['b3_value'] = Constants.s1_b1[2]
        self.participant.vars['b4_value'] = Constants.s1_b1[3]
        self.participant.vars['b5_value'] = Constants.s1_b1[4]

        self.participant.vars['var1'] = Constants.var1
        self.participant.vars['var11'] = Constants.var11
        self.participant.vars['var2'] = Constants.var2
        self.participant.vars['var22'] = Constants.var22
        self.participant.vars['var3'] = Constants.var3
        self.participant.vars['var33'] = Constants.var33
        self.participant.vars['var4'] = Constants.var4
        self.participant.vars['var44'] = Constants.var44
        self.participant.vars['var5'] = Constants.var5
        self.participant.vars['var55'] = Constants.var55


class OutcomeHL(Page):
# values needed to inform subjects about the actual outcome
    def vars_for_template(self):
            # retrieve values from participant.vars and store them in a dictionary
            return{
            'payoff_HL': self.player.participant.vars['payoff_HL'],#payoff
            'row': self.player.participant.vars['HL_row'], # randomly chosen row
            'value': self.participant.vars['HL_random'],# randomly chosen value to define outcome
            'value2': self.participant.vars['HL_scenario'],
            'choice': self.participant.vars['HL_choice_s1'],# actual choice
            # outcomes of the selected row
            'a1_value': Constants.s1_a1[self.participant.vars['HL_row'] - 1],
            'a2_value': Constants.s1_a2[self.participant.vars['HL_row'] - 1],
            'a3_value': Constants.s1_a3[self.participant.vars['HL_row'] - 1],
            'a4_value': Constants.s1_a4[self.participant.vars['HL_row'] - 1],
            'a5_value': Constants.s1_a5[self.participant.vars['HL_row'] - 1],

            'b1_value': Constants.s1_b1[0],
            'b2_value': Constants.s1_b1[1],
            'b3_value': Constants.s1_b1[2],
            'b4_value': Constants.s1_b1[3],
            'b5_value': Constants.s1_b1[4],

            'p_A_1': self.participant.vars['HL_row'],
            'p_A_2': 10-self.participant.vars['HL_row'],
            'p_B_1': self.participant.vars['HL_row'],
            'p_B_2': 10-self.participant.vars['HL_row'],
            'ist_value':Constants.ist[self.participant.vars['HL_row'] - 1],
            'var1': -Constants.var1 * 100,
            'var11': -Constants.var11 * 100,
            'var2': -Constants.var2 * 100,
            'var22': -Constants.var22 * 100,
            'var3': -Constants.var3 * 100,
            'var33': Constants.var33 * 100,
            'var4': +Constants.var44 * 100,
            'var44': +Constants.var44 * 100,
            'var5': +Constants.var5 * 100,
            'var55': +Constants.var55 * 100,

            }
    def before_next_page(self):
        self.participant.vars['ist_value'] = Constants.ist[self.participant.vars['HL_row'] - 1]


page_sequence = [
    Page0,
    ISTPage1,
    ISTPage2,
    ISTPage3,
    ISTPage4,
    IstruzioniPage1,
    IstruzioniPage3bis,
    EsempioPage3,
    EsempioPage4,
    IstruzioniPage4,
    IstruzioniPage5,
    EsempioPage1,
    EsempioPage2,
    Quiz1,
    Quiz1Right,
    Quiz2,
    Quiz2Right,
    Quiz2bis,
    Esperti,
    MyWaitPage,
    HL_Page1,
    OutcomeHL
]
