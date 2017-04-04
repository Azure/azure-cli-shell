# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
from codecs import open
from setuptools import setup

DEPENDENCIES = [
    'applicationinsights',
    'azure-cli',
    'jmespath',
    'prompt_toolkit',
    'pylint',
    'pyyaml',
    'six',
]

with open('README.rst', 'r', encoding='utf-8') as f:
    README = f.read()
with open('HISTORY.rst', 'r', encoding='utf-8') as f:
    HISTORY = f.read()

__version__ = '0.1.1a29'

setup(
    name='azure-cli-shell',
    version=__version__,
    description='Microsoft Azure Command-Line Interactive Shell',
    long_description=README + '\n\n' + HISTORY,
    license='MIT',
    author='Microsoft Corporation',
    author_email='azpycli@microsoft.com',
    scripts=['az-shell.bat', 'az-shell'],
    packages=[
        "azclishell", "linter"
    ],
    url='https://github.com/oakeyc/azure-cli-interactive-shell',
    install_requires=DEPENDENCIES,
)
