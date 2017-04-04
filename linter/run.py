# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import argparse
import os.path
import sys
from subprocess import call

import linter.path as automation_path


def run_pylint():
    print('\n\nRun pylint')

    arguments = 'azclishell'

    return_code = call(('python -m pylint ' + arguments).split())

    if return_code:
        print('Pylint failed')
    else:
        print('Pylint passed')

    return return_code


def run_pep8():
    arguments = 'azclishell'

    command = 'flake8 --statistics --append-config={} {}'.format(
        os.path.join(automation_path.get_repo_root(), '.flake8'),
        arguments)

    return_code = call((command).split())
    if return_code:
        print('Flake8 failed')
    else:
        print('Flake8 passed')

    return return_code


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Code style tools')
    parser.add_argument('--ci', action='store_true', help='Run in CI mode')
    parser.add_argument('--pep8', dest='suites', action='append_const', const='pep8',
                        help='Run flake8 to check PEP8')
    parser.add_argument('--pylint', dest='suites', action='append_const', const='pylint',
                        help='Run pylint')
    parser.add_argument('--module', dest='modules', action='append',
                        help='The modules on which the style check should run. Accept short names, '
                             'except azure-cli, azure-cli-core and azure-cli-nspkg')
    args = parser.parse_args()

    return_code_sum = run_pylint()
    code = run_pep8()
    return_code_sum += code
    sys.exit(return_code_sum)
