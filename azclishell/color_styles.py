import platform

from prompt_toolkit.styles import style_from_dict
from pygments.token import Token


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
