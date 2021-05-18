from os import environ


SESSION_CONFIGS = [
    dict(
        name='TestNewTask',
        display_name="TestNewTask",
        num_demo_participants=2,
        app_sequence=['Intro','Fase1NEW','Fase2NEW', 'Fase3NEW','Fase4','FinalPayment']
     ),
    dict(
        name='TestNewMPL',
        display_name="TestNewMPL",
        num_demo_participants=2,
        app_sequence=['Fase2NEW', 'Fase3NEW','FinalPaymentMPL']
     ),

]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'EUR'
USE_POINTS = False

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = 'd*234n^cxml5nkk09#r0%&%8$kt)pwi3qq)8jk36ts*y)nk)kf'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']

PARTICIPANT_FIELDS = ['applearea']
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
