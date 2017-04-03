#!usr/bin/env python

from __future__ import print_function

import sys
import os
from subprocess import check_call, CalledProcessError

# root_dir = os.path.abspath(os.path.join(os.path.abspath(__file__), '..', '..'))
root_dir = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


def exec_command(command):
    try:
        print('Executing: ' + command)
        check_call(command.split(), cwd=root_dir)
        print()
    except CalledProcessError as err:
        print(err, file=sys.stderr)
        sys.exit(1)

print('Running dev setup...')
print('Root directory \'{}\'\n'.format(root_dir))

# install general requirements
exec_command('pip install -r requirements.txt')

exec_command('pip install -e .')

print('Finished dev setup.')