# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import datetime
import json

from azclishell.configuration import CONFIGURATION, get_config_dir

SHELL_CONFIG = CONFIGURATION

with open(os.path.join(get_config_dir(), SHELL_CONFIG.get_frequency()), 'r') as freq:
    try:
        frequency = json.load(freq)
    except ValueError:
        frequency = {}


with open(os.path.join(get_config_dir(), SHELL_CONFIG.get_frequency()), 'w') as freq:
    now = datetime.datetime.now()
    now = now.strftime("%Y-%m-%d")
    val = frequency.get(now)
    frequency[now] = val + 1 if val else 1
    json.dump(frequency, freq)


frequent_user = True
