import platform

from prompt_toolkit.styles import style_from_dict
from pygments.token import Token

# pylint: disable=R0913
def color_mapping(curr_completion, completion, prompt, command, subcommand,
                  param, text, line, example, toolbar):

    return style_from_dict({
        # Completion colors
        Token.Menu.Completions.Completion.Current: curr_completion,
        Token.Menu.Completions.Completion: completion,
        Token.Menu.Completions.ProgressButton: 'bg:#b78991',
        Token.Menu.Completions.ProgressBar: 'bg:#ffc0cb',

        Token.Az: prompt,
        Token.Prompt.Arg: prompt,

        # Pretty Words
        Token.Keyword: command,
        Token.Keyword.Declaration: subcommand,
        Token.Name.Class: param,
        Token.Text: text,

        Token.Line: line,
        Token.Number: example,
        # toolbar
        Token.Operator: toolbar,
        Token.Toolbar: toolbar
    })


def no_style_wrapper():
    """ wraps for a no colors function """
    return None


def default_style():
    """ Default coloring """
    if platform.system() == 'Windows':
        styles = color_mapping(
            'bg:#7c2c80 #ffffff',
            'bg:#00b7b7 #ffffff',
            '#7c2c80',
            '#965699',
            '#ab77ad',
            '#c49fc5',
            '#0f5050',
            '#E500E5',
            '#00ffff',
            'bg:#000000 #ffffff')

    else:
        styles = color_mapping(
            'bg:#7c2c80 #ffffff',
            'bg:#00b7b7 #ffffff',
            '#7c2c80',
            '#965699',
            '#ab77ad',
            '#c49fc5',
            '#666666',
            '#E500E5',
            '#3d79db',
            'bg:#000000 #ffffff')

    return styles


def quiet_style():
    """ a quiet color palette """
    return color_mapping(
        'bg:#6D929B #ffffff',
        'bg:#00b7b7 #ffffff',
        '#6D929B',
        '#C1DAD6',
        '#ACD1E9',
        '#B7AFA3',
        '#666666',
        '#6D929B',
        '#C1DAD6',
        'bg:#000000 #ffffff')


def purple_style():
    """ a purple palette """
    return color_mapping(
        'bg:#C3C3E5 #ffffff',
        'bg:#8C489F #ffffff',
        '#8C489F',
        '#443266',
        '#443266',
        '#443266',
        '#C3C3E5',
        '#C3C3E5',
        '#C3C3E5',
        'bg:#000000 #ffffff')


def high_contrast_style():
    """ a high contrast palette """
    return color_mapping(
        'bg:#DD1111 #ffffff',
        'bg:#CC0000 #ffffff',
        '#3333FF',
        '#FFCC00',
        '#FFCC00',
        '#FFCC00',
        '#99FF00',
        '#99FF00',
        '#99FF00',
        'bg:#000000 #ffffff')


def pastel_style():
    return style_from_dict({
        # Completion colors
        Token.Menu.Completions.Completion.Current: 'bg:#56BAEC #ffffff',
        Token.Menu.Completions.Completion: 'bg:#B4D8E7 #ffffff',
        Token.Menu.Completions.ProgressButton: 'bg:#b78991',
        Token.Menu.Completions.ProgressBar: 'bg:#ffc0cb',

        Token.Az: '#FFAEAE',
        Token.Prompt.Arg: '#B0E57C',

        # Pretty Words
        Token.Keyword: '#FFEC94',
        Token.Keyword.Declaration: '#FFEC94',
        Token.Name.Class: '#FFEC94',
        Token.Text: '#B4D8E7',

        Token.Line: '#FFF0AA',
        Token.Number: '#FFF0AA',
        # toolbar
        Token.Operator: 'bg:#000000 #ffffff',
        Token.Toolbar: 'bg:#000000 #ffffff'
    })


def halloween_style():
    """ halloween colors """
    return style_from_dict({
        # Completion colors
        Token.Menu.Completions.Completion.Current: 'bg:#7A3E48 #ffffff',
        Token.Menu.Completions.Completion: 'bg:#3D3242 #ffffff',
        Token.Menu.Completions.ProgressButton: 'bg:#b78991',
        Token.Menu.Completions.ProgressBar: 'bg:#ffc0cb',

        Token.Az: '#3D3242',
        Token.Prompt.Arg: '#3D3242',

        # Pretty Words
        Token.Keyword: '#7A3E48',
        Token.Keyword.Declaration: '#7A3E48',
        Token.Name.Class: '#B95835',
        Token.Text: '#E18942',

        Token.Line: '#EECD86',
        Token.Number: '#EECD86',
        # toolbar
        Token.Operator: 'bg:#000000 #ffffff',
        Token.Toolbar: 'bg:#000000 #ffffff'
    })


def dark_style():
    return color_ma


OPTIONS = {
    'quiet' : quiet_style,
    'purple' : purple_style,
    'default' : default_style,
    'none' : no_style_wrapper,
    'contrast' : high_contrast_style,
    'pastel' : pastel_style,
    'halloween' : halloween_style
}


def style_factory(style):
    """ returns the proper style """
    return OPTIONS[style]() if style in OPTIONS else default_style()


def get_options():
    """ all the color options """
    return OPTIONS.keys()

