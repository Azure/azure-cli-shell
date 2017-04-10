import platform

from prompt_toolkit.styles import style_from_dict
from pygments.token import Token


def no_style_wrapper():
    """ wraps for a no colors function """
    return None


def default_style():
    """ Default coloring """
    if platform.system() == 'Windows':
        styles = style_from_dict({
            # Completion colors
            Token.Menu.Completions.Completion.Current: 'bg:#7c2c80 #ffffff',
            Token.Menu.Completions.Completion: 'bg:#00b7b7 #ffffff',
            Token.Menu.Completions.ProgressButton: 'bg:#b78991',
            Token.Menu.Completions.ProgressBar: 'bg:#ffc0cb',

            Token.Az: '#7c2c80',
            Token.Prompt.Arg: '#888888',

            # Pretty Words
            Token.Keyword: '#965699',
            Token.Keyword.Declaration: '#ab77ad',
            Token.Name.Class: '#c49fc5',
            Token.Text: '#0f5050',

            Token.Line: '#E500E5',
            Token.Number: '#00ffff',
            # toolbar
            Token.Operator: 'bg:#000000 #ffffff',
            Token.Toolbar: 'bg:#000000 #ffffff'
        })

    else:
        styles = style_from_dict({
            # Completion colors
            Token.Menu.Completions.Completion.Current: 'bg:#7c2c80 #ffffff',
            Token.Menu.Completions.Completion: 'bg:#00b7b7 #ffffff',
            Token.Menu.Completions.ProgressButton: 'bg:#b78991',
            Token.Menu.Completions.ProgressBar: 'bg:#ffc0cb',

            Token.Az: '#7c2c80',
            Token.Prompt.Arg: '#888888',

            # Pretty Words
            Token.Keyword: '#965699',
            Token.Keyword.Declaration: '#ab77ad',
            Token.Name.Class: '#c49fc5',
            Token.Text: '#666666',

            Token.Line: '#E500E5',
            Token.Number: '#3d79db',
            # toolbar
            Token.Operator: 'bg:#000000 #ffffff',
            Token.Toolbar: 'bg:#000000 #ffffff'
        })

    return styles


def quiet_style():
    """ a quiet color palette """
    return style_from_dict({
        # Completion colors
        Token.Menu.Completions.Completion.Current: 'bg:#6D929B #ffffff',
        Token.Menu.Completions.Completion: 'bg:#00b7b7 #ffffff',
        Token.Menu.Completions.ProgressButton: 'bg:#b78991',
        Token.Menu.Completions.ProgressBar: 'bg:#ffc0cb',

        Token.Az: '#6D929B',
        Token.Prompt.Arg: '#E8D0A9',

        # Pretty Words
        Token.Keyword: '#C1DAD6',
        Token.Keyword.Declaration: '#ACD1E9',
        Token.Name.Class: '#B7AFA3',
        Token.Text: '#666666',

        Token.Line: '#6D929B',
        Token.Number: '#C1DAD6',
        # toolbar
        Token.Operator: 'bg:#000000 #ffffff',
        Token.Toolbar: 'bg:#000000 #ffffff'
    })

def purple_style():
    """ a purple palette """
    return style_from_dict({
        # Completion colors
        Token.Menu.Completions.Completion.Current: 'bg:#C3C3E5 #ffffff',
        Token.Menu.Completions.Completion: 'bg:#8C489F #ffffff',
        Token.Menu.Completions.ProgressButton: 'bg:#b78991',
        Token.Menu.Completions.ProgressBar: 'bg:#ffc0cb',

        Token.Az: '#8C489F',
        Token.Prompt.Arg: '#8C489F',

        # Pretty Words
        Token.Keyword: '#443266',
        Token.Keyword.Declaration: '#443266',
        Token.Name.Class: '#443266',
        Token.Text: '#C3C3E5',

        Token.Line: '#C3C3E5',
        Token.Number: '#C3C3E5',
        # toolbar
        Token.Operator: 'bg:#000000 #ffffff',
        Token.Toolbar: 'bg:#000000 #ffffff'
    })


def high_contrast_style():
    """ a high contrast palette """
    return style_from_dict({
        # Completion colors
        Token.Menu.Completions.Completion.Current: 'bg:#DD1111 #ffffff',
        Token.Menu.Completions.Completion: 'bg:#CC0000 #ffffff',
        Token.Menu.Completions.ProgressButton: 'bg:#b78991',
        Token.Menu.Completions.ProgressBar: 'bg:#ffc0cb',

        Token.Az: '#3333FF',
        Token.Prompt.Arg: '#3333FF',

        # Pretty Words
        Token.Keyword: '#FFCC00',
        Token.Keyword.Declaration: '#FFCC00',
        Token.Name.Class: '#FFCC00',
        Token.Text: '#99FF00',

        Token.Line: '#99FF00',
        Token.Number: '#99FF00',
        # toolbar
        Token.Operator: 'bg:#000000 #ffffff',
        Token.Toolbar: 'bg:#000000 #ffffff'
    })


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


OPTIONS = {
    'quiet' : quiet_style,
    'purple' : purple_style,
    'default' : default_style,
    'none' : no_style_wrapper,
    'contrast' : high_contrast_style,
    'pastel' : pastel_style
}


def style_factory(style):
    """ returns the proper style """
    return OPTIONS[style]() if style in OPTIONS else default_style()


def get_options():
    """ all the color options """
    return OPTIONS.keys()

