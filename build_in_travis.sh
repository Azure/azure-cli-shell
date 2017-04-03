#!/usr/bin/env bash

# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

set -e

# PyLint does not yet support Python 3.6 https://github.com/PyCQA/pylint/issues/1241
if [ "$TRAVIS_PYTHON_VERSION" != "3.6" ]; then
    python -m unittest discover -s test
    # python -m linter.run "$@"

else
    python -m unittest discover -s test -p 'test_*.py'
fi

