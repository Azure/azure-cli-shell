"""
Configuration settings
"""
import os

from six.moves import configparser

SELECT_SYMBOL = {
    'outside' : '#',
    'query' : '?',
    'example' : '::',
    'exit_code' : '$',
    'default' : '%%',
    'undefault' : '^^'
}

GESTURE_INFO = {
    SELECT_SYMBOL['outside'] + "[cmd]" : "use commands outside the application",
    SELECT_SYMBOL['query'] + "[path]" : "query previous command using jmespath syntax",
    "[cmd] " + SELECT_SYMBOL['example'] + " [num]" : "do a step by step tutorial of example",
    SELECT_SYMBOL['exit_code'] : "get the exit code of the previous command",
    SELECT_SYMBOL['default'] : "default a scope",
    SELECT_SYMBOL['undefault'] : "undefault a scope",
    "Crtl+N" : "Scroll down the documentation",
    "Crtl+Y" : "Scroll up the documentation"
}

CONFIG_FILE_NAME = 'shell-config'

GESTURE_LENGTH = 20

def help_text(values):
    result = ""
    for key in values:
        result += key + ' '.join('' for x in range(GESTURE_LENGTH - len(key))) +\
                  ': ' + values[key] + '\n'
    return result

SHELL_HELP = help_text(GESTURE_INFO)

class Configuration(object):
    """ configuration for program """
    BOOLEAN_STATES = {'1': True, 'yes': True, 'true': True, 'on': True,
                      '0': False, 'no': False, 'false': False, 'off': False,
                      'y': True, 'Y': True, 'n': False, 'N': False}

    """ Configuration information """
    def __init__(self):
        self.config = configparser.ConfigParser({
            'firsttime' : 'yes',
            'colors' : 'yes'
        })
        self.config.add_section('Help Files')
        self.config.add_section('Layout')
        self.config.set('Help Files', 'command', 'help_dump.json')
        self.config.set('Help Files', 'history', 'history.txt')
        self.config.set('Layout', 'command_description', 'yes')
        self.config.set('Layout', 'param_description', 'yes')
        self.config.set('Layout', 'examples', 'yes')

        azure_folder = get_config_dir()
        if not os.path.exists(azure_folder):
            os.makedirs(azure_folder)
        if not os.path.exists(os.path.join(get_config_dir(), CONFIG_FILE_NAME)):
            with open(os.path.join(get_config_dir(), CONFIG_FILE_NAME), 'w') as config_file:
                self.config.write(config_file)
        else:
            with open(os.path.join(get_config_dir(), CONFIG_FILE_NAME), 'r') as config_file:
                self.config.readfp(config_file)  # pylint: disable=deprecated-method
                self.update()

    def get_history(self):
        """ returns the history """
        return self.config.get('Help Files', 'history')

    def get_help_files(self):
        """ returns where the command table is cached """
        return self.config.get('Help Files', 'command')

    def load(self, path):
        """ loads the configuration settings """
        self.config.read(path)

    def firsttime(self):
        """ sets it as already done"""
        self.config.set('DEFAULT', 'firsttime', 'no')
        self.update()

    def set_val(self, direct, section, val):
        """ set the config values """
        self.config.set(direct, section, val)
        self.update()

    def update(self):
        """ updates the configuration settings """
        with open(os.path.join(get_config_dir(), CONFIG_FILE_NAME), 'w') as config_file:
            self.config.write(config_file)

def get_config_dir():
    """ gets the directory of the configuration """
    if os.getenv('AZURE_CONFIG_DIR'):
        return os.getenv('AZURE_CONFIG_DIR')
    else:
        return os.path.expanduser(os.path.join('~', '.azure-shell'))
CONFIGURATION = Configuration()
