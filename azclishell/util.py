# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


import os
import sys
import platform

from prompt_toolkit.styles import style_from_dict
from pygments.token import Token


def get_window_dim():
    """ gets the dimensions depending on python version and os"""
    version = sys.version_info

    if platform.system() == 'Windows' or version >= (3, 3):
        return _size_36_windows()
    else:
        return _size_27()


def _size_27():
    """ works for python """
    dim = os.popen('stty size', 'r').read().split()
    return dim[0], dim[1]


def _size_36_windows():
    """ returns the rows, columns of terminal """
    from shutil import get_terminal_size  # pylint: disable=no-name-in-module
    dim = get_terminal_size()
    if isinstance(dim, list):
        return dim[0], dim[1]
    return dim.lines, dim.columns


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


def parse_quotes(cmd, quotes=True):
    """ parses quotes """
    string_literals = ['\'', '\"']
    args = []
    words = cmd
    open_q = False
    if quotes:
        for quote in string_literals:
            if quote in cmd:
                if cmd.count(quote) % 2 != 0:
                    raise ValueError("Invalid input: all quotes need accompanied closing quote")
                while quote in words:
                    if words.partition(quote)[0] is None:
                        break
                    if open_q:
                        args.append(words.partition(quote)[0])
                        open_q = False
                    else:
                        args.extend(words.partition(quote)[0].split())
                        open_q = True

                    words = words.partition(quote)[2]
                if words is not "":
                    args.extend(words.split())
                break
        else:
            args.extend(words.split())
    else:
        args = words.split()
    return args
