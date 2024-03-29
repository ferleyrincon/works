from os import environ
#import importlib.util


#if environ.get('OTREE_PRODUCTION') not in {None, '', '0'}:
#    DEBUG = False
#    APPS_DEBUG = False
#else:
#    DEBUG = True
#    APPS_DEBUG = True   # also enables random fill in of forms


# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

SESSION_CONFIGS = [
#    dict(
#       name='questions',
#       display_name="questions",
#       num_demo_participants=1,
#       app_sequence=['iat','survey' ]
#    ),
#    dict(
#       name='pruebas',
#       display_name="pruebas",
#       num_demo_participants=1,
#       app_sequence=['survey']
#    ),
]

#BROWSER_COMMAND = '/usr/bin/chromium-browser'

#ROOM_DEFAULTS = {}

#ROOMS = [
#    dict(
#        name='PC',
#        display_name='PC',
#        participant_label_file='_rooms/PC.txt',
#    ),
#        dict(
#        name='PC2',
#        display_name='PC2',
#        participant_label_file='_rooms/PC2.txt',
#    ),
#        dict(
#        name='PC3',
#        display_name='PC3',
#        participant_label_file='_rooms/PC3.txt',
#    ),
#]

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'es'
#TIME_ZONE = 'UTC'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'COP'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '<SET_KEY_HERE>'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']

#if importlib.util.find_spec('otreeutils'):
#    INSTALLED_APPS.append('otreeutils')

#    if importlib.util.find_spec('pandas'):
#        ROOT_URLCONF = 'iat.urls'
