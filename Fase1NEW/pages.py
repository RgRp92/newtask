from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import pandas as pd
import random
import json
from random import choices

def get_beldat(page_obj):

    farm_dat = page_obj.session.vars["beliefs_farm_dat"]

    bin_labels = [str(farm_dat["alt" + str(b)].iloc[0]) for b in range(1,6) if str(farm_dat["alt" + str(b)].iloc[0]) != "nan"]
    alt_labels = [str(farm_dat["alt" + str(b)].iloc[0]) for b in range(1,6) if str(farm_dat["alt" + str(b)].iloc[0]) != "nan"]

    # If bin_button is empty, don't show the button to toggle alt labels
    bin_button = str(farm_dat["bin_button"].iloc[0]).strip()
    bin_button = bin_button if bin_button != "nan" else ""
    pay_by = str(farm_dat["pay_by"].iloc[0]).strip()

    beldat = {
        "tokens": int(farm_dat["tokens"].iloc[0]),
        "alpha": float(farm_dat["alpha"].iloc[0]),
        "delta": float(farm_dat["delta"].iloc[0]),
        "currency": str(farm_dat["currency"].iloc[0]),
        "text": str(farm_dat["text"].iloc[0]),
        "alt_text": str(farm_dat["alt_text"].iloc[0]),
        "bin_button": bin_button,
        "alt_button": str(farm_dat["alt_button"].iloc[0]),
        "pay_by": pay_by,
        "bin_labels": bin_labels,
        "alt_labels": alt_labels,
        "num_bins": len(bin_labels),
    }

    # Store this data in the round data
    page_obj.participant.vars["beliefs_round_data"].append(beldat)
    return(beldat)

def set_beliefs_data(page_obj):
    nrounds = [1,2,3]
    nrounds = len(nrounds)
    page_obj.participant.vars["beliefs_num_rounds"] = nrounds

class Page0(Page):
    def vars_for_template(self):
            # Set the belief data for the participant
        set_beliefs_data(self)

    def is_displayed(self):
        return self.round_number == 1

class Page1FarmerInfo(Page):
    def vars_for_template(self):
        # Set the belief data for the participant
        set_beliefs_data(self)

    def is_displayed(self):
        return self.round_number == 1

class Page2Interval(Page):
    def vars_for_template(self):
            # Set the belief data for the participant
        set_beliefs_data(self)

    def is_displayed(self):
        return self.round_number == 1

class Page3Strumento(Page):
    def vars_for_template(self):
            # Set the belief data for the participant
        set_beliefs_data(self)

    def is_displayed(self):
        return self.round_number == 1

class Page4Payoff(Page):
    def vars_for_template(self):
            # Set the belief data for the participant
        set_beliefs_data(self)

    def is_displayed(self):
        return self.round_number == 1

class Page5Esempio1(Page):
    def vars_for_template(self):
            # Set the belief data for the participant
        set_beliefs_data(self)

    def is_displayed(self):
        return self.round_number == 1

class Page6Esempio1Payoff(Page):
    def vars_for_template(self):
            # Set the belief data for the participant
        set_beliefs_data(self)

    def is_displayed(self):
        return self.round_number == 1

class Page7Esempio2(Page):
    def vars_for_template(self):
            # Set the belief data for the participant
        set_beliefs_data(self)

    def is_displayed(self):
        return self.round_number == 1

class Page8Esempio2Payoff(Page):
    def vars_for_template(self):
            # Set the belief data for the participant
        set_beliefs_data(self)

    def is_displayed(self):
        return self.round_number == 1

class Page9QuizPage(Page):
    form_model = 'player'
    form_fields = ['quizf1']

    def vars_for_template(self):
            # Set the belief data for the participant
        set_beliefs_data(self)

    def before_next_page(self):
        self.participant.vars['quizf1'] = self.player.quizf1

    def is_displayed(self):
        return self.round_number == 1

class Page9QuizPageRight(Page):
    form_model = 'player'

    def vars_for_template(self):
            # Set the belief data for the participant
        set_beliefs_data(self)

    def is_displayed(self):
        return self.round_number == 1 and self.participant.vars['quizf1'] == '1'

class Page9Quiz2Page(Page):
    form_model = 'player'
    form_fields = ['quiz2f1']

    def vars_for_template(self):
            # Set the belief data for the participant
        set_beliefs_data(self)

    def before_next_page(self):
        self.participant.vars['quiz2f1'] = self.player.quiz2f1

    def is_displayed(self):
        return self.round_number == 1 and self.participant.vars["quizf1"] != '1'

class Page9Quiz2PageRight (Page):
    form_model = 'player'

    def vars_for_template(self):
            # Set the belief data for the participant
        set_beliefs_data(self)

    def is_displayed(self):
        return self.round_number == 1 and self.participant.vars["quizf1"] != '1' and self.participant.vars['quiz2f1'] == '1'

class Page9Quiz2bisPage(Page):
    form_model = 'player'

    def vars_for_template(self):
            # Set the belief data for the participant
        set_beliefs_data(self)

    def is_displayed(self):
        return self.round_number == 1 and self.participant.vars["quizf1"] != '1' and self.participant.vars['quiz2f1'] != '1'

class Page9Quiz3Page(Page):
    form_model = 'player'
    form_fields = ['quiz3f1']

    def vars_for_template(self):
            # Set the belief data for the participant
        set_beliefs_data(self)

    def before_next_page(self):
        self.participant.vars['quiz3f1'] = self.player.quiz3f1
        
    def is_displayed(self):
        return self.round_number == 1

class Page9Quiz3PageRight(Page):
    form_model = 'player'

    def vars_for_template(self):
            # Set the belief data for the participant
        set_beliefs_data(self)

    def is_displayed(self):
        return self.round_number == 1 and  self.participant.vars["quiz3f1"] == '1'

class Page9Quiz4Page(Page):
    form_model = 'player'
    form_fields = ['quiz4f1']

    def vars_for_template(self):
            # Set the belief data for the participant
        set_beliefs_data(self)

    def before_next_page(self):
        self.participant.vars['quiz4f1'] = self.player.quiz4f1
    def is_displayed(self):
        return self.round_number == 1 and  self.participant.vars["quiz3f1"] != '1'

class Page9Quiz4PageRight(Page):
    form_model = 'player'

    def vars_for_template(self):
            # Set the belief data for the participant
        set_beliefs_data(self)

    def is_displayed(self):
        return self.round_number == 1 and  self.participant.vars["quiz3f1"] != '1'and self.participant.vars["quiz4f1"] == '1'

class Page9Quiz4bisPage(Page):
    form_model = 'player'

    def vars_for_template(self):
            # Set the belief data for the participant
        set_beliefs_data(self)

    def is_displayed(self):
        return self.round_number == 1 and  self.participant.vars["quiz3f1"] != '1'and self.participant.vars["quiz4f1"] != '1'

class Page10ProvaStrumento(Page):
    def vars_for_template(self):
            # Set the belief data for the participant
        set_beliefs_data(self)

    form_model = "player"

    def initial_values(self):
        rnum = self.round_number
        if rnum == 1 and "beldat_is_set" not in self.participant.vars:
            # Record the choices for every round here
            self.participant.vars["beliefs_choice"] = []
            # Record the data for each choice
            self.participant.vars["beliefs_round_data"] = []

    def get_form_fields(self):
        # Set initial values for this participant
        self.initial_values()
        # The belief data
        beldat = get_beldat(self)
        # Add the labelset val as wel
        form_fields = ["bin" + str(i) for i in range(1, len(beldat["alt_labels"]) + 1)] + ["labelset"]
        return(form_fields)

    def vars_for_template(self):
        # Set initial values for this participant
        self.initial_values()

        # The lottery data for this row
        beldat = get_beldat(self)

        beliefs = {"round_number"    : self.round_number,
                   "number_of_rounds": self.participant.vars["beliefs_num_rounds"],
                   "hex_colors"      : self.session.vars["beliefs_hex_colors"],
                   "beldat"          : beldat,
                   "tokens"          : beldat["tokens"],
                   "currency"        : beldat["currency"],
                   "task_number"     : 1,
                   }
        return {
            "beliefs": beliefs,
        }

    def is_displayed(self):
        return self.round_number == 1

class Page11Esperti(Page):
    def is_displayed(self):
        return self.round_number == 1

class Page12Ripetere(Page):
    def is_displayed(self):
        return self.round_number == 1

class Page13Ripetere2(Page):
    def is_displayed(self):
        return self.round_number == 1

class Page14Ripetere3(Page):
    def is_displayed(self):
        return self.round_number == 1
class Page14Ripetere3b(Page):
    def is_displayed(self):
        return self.round_number == 1
class Page14Ripetere3c(Page):
    def is_displayed(self):
        return self.round_number == 1
class Page14Ripetere4(Page):
    def is_displayed(self):
        return self.round_number == 1

class Page20RipEsemp3a(Page):
    def vars_for_template(self):
            # Set the belief data for the participant
        set_beliefs_data(self)

    def is_displayed(self):
        return self.round_number == 1

class Page21RipEsemp3b(Page):
    def vars_for_template(self):
            # Set the belief data for the participant
        set_beliefs_data(self)

    def is_displayed(self):
        return self.round_number == 1

class Page22RipEsemp3c(Page):
    def vars_for_template(self):
            # Set the belief data for the participant
        set_beliefs_data(self)

    def is_displayed(self):
        return self.round_number == 1

class Page22RipEsemp3e(Page):
    def vars_for_template(self):
            # Set the belief data for the participant
        set_beliefs_data(self)

    def is_displayed(self):
        return self.round_number == 1

class Page22RipEsemp3f(Page):
    def vars_for_template(self):
            # Set the belief data for the participant
        set_beliefs_data(self)

    def is_displayed(self):
        return self.round_number == 1

class Page23MyWaitPage(Page):
    def is_displayed(self):
        return self.round_number == 1

class Page24FarmerChoice(Page):
    form_model = "player"
    form_fields = ["rip1","rip2"]

    def initial_values(self):
        rnum = self.round_number
        # Randomize the data if we're in the first round
        if rnum == 1 and "beldat_is_set" not in self.participant.vars:
            self.participant.vars["beldat_is_set"] = True
            # Record the choices for every round here
            self.participant.vars["beliefs_choice"] = []
            # Record the data for each choice
            self.participant.vars["beliefs_round_data"] = []

    def get_form_fields(self):
        # Set initial values for this participant
        self.initial_values()
        # The belief data
        beldat = get_beldat(self)
        # Add the labelset val as wel
        form_fields = ["bin" + str(i) for i in range(1, len(beldat["bin_labels"]) + 1)] + ["labelset"]
        return(form_fields)

    def vars_for_template(self):
        # Set initial values for this participant


        self.initial_values()

        # The lottery data for this row
        beldat = get_beldat(self)


        beliefs = {"round_number"    : self.round_number,
                   "number_of_rounds": self.participant.vars["beliefs_num_rounds"],
                   "hex_colors"      : self.session.vars["beliefs_hex_colors"],
                   "beldat"          : beldat,
                   "tokens"          : beldat["tokens"],
                   "currency"        : beldat["currency"],
                   "task_number"     : 1,
               }


        return {
            "beliefs": beliefs,
            }


    def before_next_page(self):
        choice = [getattr(self.player, "bin" + str(b)) for b in range(1,6)]
        self.participant.vars["beliefs_choice"].append(choice)

    def is_displayed(self):
       return self.round_number <= self.participant.vars["beliefs_num_rounds"]

    def app_after_this_page(self, upcoming_apps):
        if self.player.rip1 == '0':
            return 'Fase2NEW'

class Page25Repeat1(Page):
    form_model = "player"
    form_fields = ["rip1"]

    def vars_for_template(self):
        choices_made = self.participant.vars["beliefs_choice"]

        pay_choices = choices_made[0]
        pay_round = pay_choices

        # The lottery data for this row
        beldat = self.participant.vars["beliefs_round_data"][0]

        # Not really used anywhere
        final_payment = {
            "currency": beldat["currency"],
            "amounts": [],
            "when": [beldat["pay_by"]],
            "choices": pay_choices,
        }
        self.participant.vars["beliefs_final_payment"] = final_payment
        setattr(self.player, "final_payment", json.dumps(final_payment))

        beliefs_results = {
            "round_number": self.round_number,
            "number_of_rounds": self.participant.vars["beliefs_num_rounds"],
            "hex_colors": self.session.vars["beliefs_hex_colors"],
            "beldat": beldat,
            "tokens": beldat["tokens"],
            "currency": beldat["currency"],
            "task_number": 6,
            "pay_round": pay_round,
            "pay_choices": pay_choices,
            "final_payment": final_payment,
        }
        # Save this data for use in the final results page
        self.participant.vars["beliefs_results"] = beliefs_results

        return {
            "beliefs": beliefs_results,

        }

    def is_displayed(self):
        return self.round_number == round(1)

    def before_next_page(self):
        self.player.set_winning_bin()
        self.participant.vars["rip_v"] = self.player.rip1

class Page26Farmer1ChoiceResult(Page):
    def vars_for_template(self):

        num_rounds = [1]
        # Select a round at random for payment
        if "beliefs_pay_round" not in self.participant.vars:
            pay_round = choices(num_rounds)
            self.participant.vars["beliefs_pay_round"] = pay_round
        else:
            pay_round = self.participant.vars["beliefs_pay_round"]

        pay_round = pay_round[0]

        prev_player = self.player.in_round(pay_round + 1)

        if self.participant.vars['nw_bin'] == "1":
            self.participant.vars['p_bin'] = prev_player.bin1
        if self.participant.vars['nw_bin'] == "2":
            self.participant.vars['p_bin'] = prev_player.bin2
        if self.participant.vars['nw_bin'] == "3":
            self.participant.vars['p_bin'] = prev_player.bin3
        if self.participant.vars['nw_bin'] == "4":
            self.participant.vars['p_bin'] = prev_player.bin4
        if self.participant.vars['nw_bin'] == "5":
            self.participant.vars['p_bin'] = prev_player.bin5


        self.player.w_amt = (12.5) + \
                            12.5 * ((2 * self.participant.vars['p_bin'] / 100) - (1 / 10000) * (
                prev_player.bin1 ** 2 + prev_player.bin2 ** 2 + prev_player.bin3 ** 2 +
                prev_player.bin4 ** 2 + prev_player.bin5 ** 2))

        w_amt = round(self.player.w_amt, 2)

        choices_made = self.participant.vars["beliefs_choice"]

        pay_choices = choices_made[0]

        # The saved choices made by the subject


        # The lottery data for this row
        beldat = self.participant.vars["beliefs_round_data"][0]

        # Not really used anywhere
        final_payment = {
            "currency": beldat["currency"],
            "amounts": [],
            "when": [beldat["pay_by"]],
            "choices": pay_choices,
        }
        self.participant.vars["beliefs_final_payment"] = final_payment
        setattr(self.player, "final_payment", json.dumps(final_payment))

        beliefs_results = {
            "round_number": self.round_number,
            "number_of_rounds": self.participant.vars["beliefs_num_rounds"],
            "hex_colors": self.session.vars["beliefs_hex_colors"],
            "beldat": beldat,
            "tokens": beldat["tokens"],
            "currency": beldat["currency"],
            "task_number": 6,
            "pay_round": pay_round,
            "pay_choices": pay_choices,
            "final_payment": final_payment,
        }
        # Save this data for use in the final results page
        self.participant.vars["beliefs_results"] = beliefs_results

        return {
            "beliefs": beliefs_results,
            "w_amt": round(w_amt, 2)
        }

    def is_displayed(self):
        return self.player.rip1 == '0'

    def before_next_page(self):
        self.participant.vars["w_amt"] = round(self.player.w_amt, 2)

    def app_after_this_page(self, upcoming_apps):
        if self.player.rip1 == '0':
            return 'Fase2NEW'

class Page27Repeat2(Page):
    form_model = "player"
    form_fields = ["rip2"]

    def vars_for_template(self):
        # The saved choices made by the subject
        choices_made = self.participant.vars["beliefs_choice"]

        pay_choices = choices_made[0]
        pay_round = pay_choices

        pay_choices_2 = choices_made[1]
        pay_round_2 = pay_choices_2

        # The lottery data for this row
        beldat = self.participant.vars["beliefs_round_data"][0]

        # Not really used anywhere
        final_payment = {
            "currency": beldat["currency"],
            "amounts": [],
            "when": [beldat["pay_by"]],
            "choices": pay_choices,
        }
        self.participant.vars["beliefs_final_payment"] = final_payment
        setattr(self.player, "final_payment", json.dumps(final_payment))

        beliefs_results = {
            "round_number": self.round_number,
            "number_of_rounds": self.participant.vars["beliefs_num_rounds"],
            "hex_colors": self.session.vars["beliefs_hex_colors"],
            "beldat": beldat,
            "tokens": beldat["tokens"],
            "currency": beldat["currency"],
            "task_number": 6,
            "pay_round": pay_round,
            "pay_choices": pay_choices,
            "final_payment": final_payment,
        }
        beliefs_results_2 = {
            "round_number": self.round_number,
            "number_of_rounds": self.participant.vars["beliefs_num_rounds"],
            "hex_colors": self.session.vars["beliefs_hex_colors"],
            "beldat": beldat,
            "tokens": beldat["tokens"],
            "currency": beldat["currency"],
            "task_number": 6,
            "pay_round": pay_round_2,
            "pay_choices": pay_choices_2,
            "final_payment": final_payment,
        }

        # Save this data for use in the final results page
        self.participant.vars["beliefs_results"] = beliefs_results

        return {
            "beliefs": beliefs_results,
            "beliefs_2": beliefs_results_2,
        }

    def is_displayed(self):
        return self.round_number == round(2)

    def before_next_page(self):
        self.participant.vars["rip_v2"] = self.player.rip2

class Page28Farmer2ChoicesUrna(Page):
    form_model = "player"
    form_fields = ['pref1', 'pref2']

    def vars_for_template(self):
        # The saved choices made by the subject
        choices_made = self.participant.vars["beliefs_choice"]

        pay_choices = choices_made[0]
        pay_round = pay_choices

        pay_choices_2 = choices_made[1]
        pay_round_2 = pay_choices_2

        # The lottery data for this row
        beldat = self.participant.vars["beliefs_round_data"][0]

        beliefs_results = {
                "round_number"    : self.round_number,
                "number_of_rounds": self.participant.vars["beliefs_num_rounds"],
                "hex_colors"      : self.session.vars["beliefs_hex_colors"],
                "beldat"          : beldat,
                "tokens"          : beldat["tokens"],
                "currency"        : beldat["currency"],
                "task_number"     : 6,
                "pay_round": pay_round,
                "pay_choices": pay_choices,
               }

        beliefs_results_2 = {
            "round_number": self.round_number,
            "number_of_rounds": self.participant.vars["beliefs_num_rounds"],
            "hex_colors": self.session.vars["beliefs_hex_colors"],
            "beldat": beldat,
            "tokens": beldat["tokens"],
            "currency": beldat["currency"],
            "task_number": 6,
            "pay_round": pay_round_2,
            "pay_choices": pay_choices_2,
        }


        # Save this data for use in the final results page
        self.participant.vars["beliefs_results"] = beliefs_results

        return {
            "beliefs": beliefs_results,
            "beliefs_2": beliefs_results_2,
        }

    def is_displayed(self):
        return self.player.rip2 == '0'

    def before_next_page(self):
        self.player.sum_token = sum([self.player.pref1, self.player.pref2])
        self.participant.vars["weights"] = [self.player.pref1, self.player.pref2]
        self.player.set_winning_bin()

class Page28Farmer2ChoicesUrna2(Page):
    form_model = "player"
    form_fields = ['pref1', 'pref2']

    def vars_for_template(self):
        # The saved choices made by the subject
        choices_made = self.participant.vars["beliefs_choice"]

        pay_choices = choices_made[0]
        pay_round = pay_choices

        pay_choices_2 = choices_made[1]
        pay_round_2 = pay_choices_2

        # The lottery data for this row
        beldat = self.participant.vars["beliefs_round_data"][0]

        beliefs_results = {
                "round_number"    : self.round_number,
                "number_of_rounds": self.participant.vars["beliefs_num_rounds"],
                "hex_colors"      : self.session.vars["beliefs_hex_colors"],
                "beldat"          : beldat,
                "tokens"          : beldat["tokens"],
                "currency"        : beldat["currency"],
                "task_number"     : 6,
                "pay_round": pay_round,
                "pay_choices": pay_choices,
               }

        beliefs_results_2 = {
            "round_number": self.round_number,
            "number_of_rounds": self.participant.vars["beliefs_num_rounds"],
            "hex_colors": self.session.vars["beliefs_hex_colors"],
            "beldat": beldat,
            "tokens": beldat["tokens"],
            "currency": beldat["currency"],
            "task_number": 6,
            "pay_round": pay_round_2,
            "pay_choices": pay_choices_2,
        }


        # Save this data for use in the final results page
        self.participant.vars["beliefs_results"] = beliefs_results

        return {
            "beliefs": beliefs_results,
            "beliefs_2": beliefs_results_2,
        }

    def is_displayed(self):
        return self.player.rip2 == '0'

    def before_next_page(self):
        self.player.sum_token = sum([self.player.pref1, self.player.pref2])
        self.player.set_winning_bin()

class Page28Farmer2ChoicesPie(Page):
    form_model = "player"

    def vars_for_template(self):
        self.participant.vars['slice1'] = round(self.player.pref1 / (sum([self.player.pref1, self.player.pref2])),1)
        self.participant.vars['slice2'] = round(self.player.pref2 / (sum([self.player.pref1, self.player.pref2])),1)


        return {
            "slice1": self.participant.vars['slice1'],
            "slice2": self.participant.vars['slice2'],
            "pref1": self.player.pref1,
            "pref2": self.player.pref2,
            "sum": sum([self.player.pref1, self.player.pref2])

        }

    def is_displayed(self):
        return self.player.rip2 == '0'

    def before_next_page(self):
        self.player.sum_token = sum([self.player.pref1, self.player.pref2])
        self.participant.vars["weights"] = [self.participant.vars['slice1'],self.participant.vars['slice2']]
        self.player.set_winning_bin()

class Page29Farmer2ChoicesResult(Page):
    form_model  = "player"

    def vars_for_template(self):

        weights = self.participant.vars["weights"]
        # The number of rounds
        num_rounds = [0,1]
        # Select a round at random for payment
        if "beliefs_pay_round" not in self.participant.vars:
            pay_round = choices(num_rounds, weights)
            self.participant.vars["beliefs_pay_round"] = pay_round
        else:
            pay_round = self.participant.vars["beliefs_pay_round"]

        pay_round = pay_round[0]

        prev_player = self.player.in_round(pay_round + 1)

        if self.participant.vars['nw_bin'] == "1":
            self.participant.vars['p_bin'] = prev_player.bin1
        if self.participant.vars['nw_bin'] == "2":
            self.participant.vars['p_bin'] = prev_player.bin2
        if self.participant.vars['nw_bin'] == "3":
            self.participant.vars['p_bin'] = prev_player.bin3
        if self.participant.vars['nw_bin'] == "4":
            self.participant.vars['p_bin'] = prev_player.bin4
        if self.participant.vars['nw_bin'] == "5":
            self.participant.vars['p_bin'] = prev_player.bin5


        self.player.w_amt = (12.5) + \
                            12.5 * ((2 * self.participant.vars['p_bin']/ 100) - (1 / 10000) * (
                prev_player.bin1 ** 2 + prev_player.bin2 ** 2 + prev_player.bin3 ** 2 +
                prev_player.bin4 ** 2 + prev_player.bin5 ** 2  ))

        w_amt = round(self.player.w_amt, 2)

        # The saved choices made by the subject
        choices_made = self.participant.vars["beliefs_choice"]
        pay_choices = choices_made[pay_round]

        # The lottery data for this row
        beldat = self.participant.vars["beliefs_round_data"][pay_round]

        # Not really used anywhere
        final_payment = {
                "currency" : beldat["currency"],
                "amounts": [],
                "when": [beldat["pay_by"]],
                "choices": pay_choices,
                }
        self.participant.vars["beliefs_final_payment"] = final_payment
        setattr(self.player, "final_payment", json.dumps(final_payment))

        beliefs_results = {
                "round_number"    : self.round_number,
                "number_of_rounds": self.participant.vars["beliefs_num_rounds"],
                "hex_colors"      : self.session.vars["beliefs_hex_colors"],
                "beldat"          : beldat,
                "tokens"          : beldat["tokens"],
                "currency"        : beldat["currency"],
                "task_number"     : 6,
                "pay_round": pay_round + 1,
                "pay_choices": pay_choices,
                "final_payment" : final_payment,
               }

        # Save this data for use in the final results page
        self.participant.vars["beliefs_results"] = beliefs_results

        return {
            "beliefs" : beliefs_results,
            "w_amt": round(w_amt,2),
            "variation": self.participant.vars["variation"],
            "nw_bin": self.participant.vars["nw_bin"],
            "p_bin": self.participant.vars['p_bin']
        }

    def is_displayed(self):
        return self.player.rip2 == '0'


    def before_next_page(self):
        self.participant.vars["w_round"]= self.participant.vars["beliefs_results"]["pay_round"]
        self.participant.vars["w_amt"]= round(self.player.w_amt,2)

    def app_after_this_page(self, upcoming_apps):
        if self.player.rip2 == '0':
            return 'Fase2NEW'

class Page28Farmer3ChoicesUrna(Page):
    form_model = "player"
    form_fields = ['pref1', 'pref2','pref3']

    def vars_for_template(self):
        # The saved choices made by the subject
        choices_made = self.participant.vars["beliefs_choice"]

        pay_choices = choices_made[0]
        pay_round = pay_choices

        pay_choices_2 = choices_made[1]
        pay_round_2 = pay_choices_2

        pay_choices_3 = choices_made[2]
        pay_round_3 = pay_choices_3

        # The lottery data for this row
        beldat = self.participant.vars["beliefs_round_data"][0]

        # Not really used anywhere
        final_payment = {
                "currency" : beldat["currency"],
                "amounts": [],
                "when": [beldat["pay_by"]],
                "choices": pay_choices,
                }
        self.participant.vars["beliefs_final_payment"] = final_payment
        setattr(self.player, "final_payment", json.dumps(final_payment))

        beliefs_results = {
                "round_number"    : self.round_number,
                "number_of_rounds": self.participant.vars["beliefs_num_rounds"],
                "hex_colors"      : self.session.vars["beliefs_hex_colors"],
                "beldat"          : beldat,
                "tokens"          : beldat["tokens"],
                "currency"        : beldat["currency"],
                "task_number"     : 6,
                "pay_round": pay_round,
                "pay_choices": pay_choices,
                "final_payment" : final_payment,
               }
        beliefs_results_2 = {
            "round_number": self.round_number,
            "number_of_rounds": self.participant.vars["beliefs_num_rounds"],
            "hex_colors": self.session.vars["beliefs_hex_colors"],
            "beldat": beldat,
            "tokens": beldat["tokens"],
            "currency": beldat["currency"],
            "task_number": 6,
            "pay_round": pay_round_2,
            "pay_choices": pay_choices_2,
            "final_payment": final_payment,
        }

        beliefs_results_3 = {
            "round_number": self.round_number,
            "number_of_rounds": self.participant.vars["beliefs_num_rounds"],
            "hex_colors": self.session.vars["beliefs_hex_colors"],
            "beldat": beldat,
            "tokens": beldat["tokens"],
            "currency": beldat["currency"],
            "task_number": 6,
            "pay_round": pay_round_3,
            "pay_choices": pay_choices_3,
            "final_payment": final_payment,
        }

        # Save this data for use in the final results page
        self.participant.vars["beliefs_results"] = beliefs_results

        return {
            "beliefs": beliefs_results,
            "beliefs_2": beliefs_results_2,
            "beliefs_3": beliefs_results_3,
        }

    def is_displayed(self):
        return self.round_number == self.participant.vars["beliefs_num_rounds"]

    def before_next_page(self):
        self.player.sum_token = sum([self.player.pref1, self.player.pref2, self.player.pref3])
        self.participant.vars["weights"] = [self.player.pref1, self.player.pref2, self.player.pref3]
        self.player.set_winning_bin()

class Page28Farmer3ChoicesUrna2(Page):
    form_model = "player"
    form_fields = ['pref1', 'pref2','pref3']

    def vars_for_template(self):
        # The saved choices made by the subject
        choices_made = self.participant.vars["beliefs_choice"]

        pay_choices = choices_made[0]
        pay_round = pay_choices

        pay_choices_2 = choices_made[1]
        pay_round_2 = pay_choices_2

        pay_choices_3 = choices_made[2]
        pay_round_3 = pay_choices_3

        # The lottery data for this row
        beldat = self.participant.vars["beliefs_round_data"][0]

        # Not really used anywhere
        final_payment = {
                "currency" : beldat["currency"],
                "amounts": [],
                "when": [beldat["pay_by"]],
                "choices": pay_choices,
                }
        self.participant.vars["beliefs_final_payment"] = final_payment
        setattr(self.player, "final_payment", json.dumps(final_payment))

        beliefs_results = {
                "round_number"    : self.round_number,
                "number_of_rounds": self.participant.vars["beliefs_num_rounds"],
                "hex_colors"      : self.session.vars["beliefs_hex_colors"],
                "beldat"          : beldat,
                "tokens"          : beldat["tokens"],
                "currency"        : beldat["currency"],
                "task_number"     : 6,
                "pay_round": pay_round,
                "pay_choices": pay_choices,
                "final_payment" : final_payment,
               }
        beliefs_results_2 = {
            "round_number": self.round_number,
            "number_of_rounds": self.participant.vars["beliefs_num_rounds"],
            "hex_colors": self.session.vars["beliefs_hex_colors"],
            "beldat": beldat,
            "tokens": beldat["tokens"],
            "currency": beldat["currency"],
            "task_number": 6,
            "pay_round": pay_round_2,
            "pay_choices": pay_choices_2,
            "final_payment": final_payment,
        }

        beliefs_results_3 = {
            "round_number": self.round_number,
            "number_of_rounds": self.participant.vars["beliefs_num_rounds"],
            "hex_colors": self.session.vars["beliefs_hex_colors"],
            "beldat": beldat,
            "tokens": beldat["tokens"],
            "currency": beldat["currency"],
            "task_number": 6,
            "pay_round": pay_round_3,
            "pay_choices": pay_choices_3,
            "final_payment": final_payment,
        }

        # Save this data for use in the final results page
        self.participant.vars["beliefs_results"] = beliefs_results

        return {
            "beliefs": beliefs_results,
            "beliefs_2": beliefs_results_2,
            "beliefs_3": beliefs_results_3,
        }

    def is_displayed(self):
        return self.round_number == self.participant.vars["beliefs_num_rounds"]

    def before_next_page(self):
        self.player.sum_token = sum([self.player.pref1, self.player.pref2, self.player.pref3])
        self.player.set_winning_bin()

class Page28Farmer3ChoicesPie(Page):
    form_model = "player"

    def vars_for_template(self):
        self.participant.vars["slice1"] = round(self.player.pref1 / (sum([self.player.pref1, self.player.pref2, self.player.pref3])),2)
        self.participant.vars["slice2"] = round(self.player.pref2 / (sum([self.player.pref1, self.player.pref2, self.player.pref3])),2)
        self.participant.vars["slice3"] = round(self.player.pref3 / (sum([self.player.pref1, self.player.pref2, self.player.pref3])),2)


        return {
            "slice1": self.participant.vars["slice1"],
            "slice2": self.participant.vars["slice2"],
            "slice3": self.participant.vars["slice3"],
            "pref1": self.player.pref1,
            "pref2": self.player.pref2,
            "pref3": self.player.pref3,
            "sum": sum([self.player.pref1, self.player.pref2, self.player.pref3])
        }

    def is_displayed(self):
        return self.round_number == self.participant.vars["beliefs_num_rounds"]

    def before_next_page(self):
        self.player.sum_token = sum([self.player.pref1, self.player.pref2,self.player.pref3])
        self.participant.vars["weights"] = [self.participant.vars["slice1"], self.participant.vars["slice2"], self.participant.vars["slice3"]]
        self.player.set_winning_bin()

class Page29Farmer3ChoicesResult(Page):
    form_model  = "player"

    def vars_for_template(self):

        weights = self.participant.vars["weights"]
        # The number of rounds
        num_rounds = [0,1,2]
        # Select a round at random for payment
        if "beliefs_pay_round" not in self.participant.vars:
            pay_round = choices(num_rounds, weights)
            self.participant.vars["beliefs_pay_round"] = pay_round
        else:
            pay_round = self.participant.vars["beliefs_pay_round"]

        pay_round = pay_round[0]

        prev_player = self.player.in_round(pay_round + 1)

        if self.participant.vars['nw_bin'] == "1":
            self.participant.vars['p_bin'] = prev_player.bin1
        if self.participant.vars['nw_bin'] == "2":
            self.participant.vars['p_bin'] = prev_player.bin2
        if self.participant.vars['nw_bin'] == "3":
            self.participant.vars['p_bin'] = prev_player.bin3
        if self.participant.vars['nw_bin'] == "4":
            self.participant.vars['p_bin'] = prev_player.bin4
        if self.participant.vars['nw_bin'] == "5":
            self.participant.vars['p_bin'] = prev_player.bin5


        self.player.w_amt = (12.5) + \
                            12.5 * ((2 * self.participant.vars['p_bin']/ 100) - (1 / 10000) * (
                prev_player.bin1 ** 2 + prev_player.bin2 ** 2 + prev_player.bin3 ** 2 +
                prev_player.bin4 ** 2 + prev_player.bin5 ** 2 ))

        w_amt = round(self.player.w_amt, 2)

        # The saved choices made by the subject
        choices_made = self.participant.vars["beliefs_choice"]
        pay_choices = choices_made[pay_round]

        # The lottery data for this row
        beldat = self.participant.vars["beliefs_round_data"][pay_round]

        # Not really used anywhere
        final_payment = {
                "currency" : beldat["currency"],
                "amounts": [],
                "when": [beldat["pay_by"]],
                "choices": pay_choices,
                }
        self.participant.vars["beliefs_final_payment"] = final_payment
        setattr(self.player, "final_payment", json.dumps(final_payment))

        beliefs_results = {
                "round_number"    : self.round_number,
                "number_of_rounds": self.participant.vars["beliefs_num_rounds"],
                "hex_colors"      : self.session.vars["beliefs_hex_colors"],
                "beldat"          : beldat,
                "tokens"          : beldat["tokens"],
                "currency"        : beldat["currency"],
                "task_number"     : 6,
                "pay_round": pay_round + 1,
                "pay_choices": pay_choices,
                "final_payment" : final_payment,
               }

        # Save this data for use in the final results page
        self.participant.vars["beliefs_results"] = beliefs_results

        return {
            "beliefs" : beliefs_results,
            "w_amt": round(w_amt,2),
            "variation": self.participant.vars["variation"],
            "nw_bin": self.participant.vars["nw_bin"],
            "p_bin": self.participant.vars['p_bin']
        }

    def is_displayed(self):
        return self.round_number == self.participant.vars["beliefs_num_rounds"]

    def before_next_page(self):
        self.participant.vars["w_round"]= self.participant.vars["beliefs_results"]["pay_round"]
        self.participant.vars["w_amt"]= round(self.player.w_amt,2)



page_sequence = [
    Page0,
    Page1FarmerInfo,
    Page2Interval,
    Page3Strumento,
    Page4Payoff,
    Page5Esempio1,
    Page6Esempio1Payoff,
    Page7Esempio2,
    Page8Esempio2Payoff,
    Page9QuizPage,
    Page9QuizPageRight,
    Page9Quiz2Page,
    Page9Quiz2PageRight,
    Page9Quiz2bisPage,
    Page10ProvaStrumento,
    Page11Esperti,
    Page12Ripetere,
    Page13Ripetere2,
    Page14Ripetere3,
    Page14Ripetere3b,
    Page14Ripetere3c,
    Page14Ripetere4,
    Page22RipEsemp3c,
    Page22RipEsemp3e,
    Page23MyWaitPage,
    Page24FarmerChoice,
    Page25Repeat1,
    Page26Farmer1ChoiceResult,
    Page27Repeat2,
    Page28Farmer2ChoicesUrna2,
    Page28Farmer2ChoicesPie,
    Page29Farmer2ChoicesResult,
    Page28Farmer3ChoicesUrna2,
    Page28Farmer3ChoicesPie,
    Page29Farmer3ChoicesResult,

]
