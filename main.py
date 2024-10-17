import json
import os
import inquirer
from collections import defaultdict
from stats_data import StatsMyData
from menu_manager import Menu
from query_data import ProcessData
from typing import Dict, List, Tuple

data = ProcessData()
parameters = defaultdict(list)
parameters['filename'] = 'data.json'
data.set_parameters(parameters)
data.process()
menu = Menu()
menu.open_menu()   