import json
import os
import threading
import inquirer
from collections import defaultdict
from StatsMyData import StatsMyData
from typing import Dict, List, Tuple, Callable

class Menu:
    def __init__(self) -> None:
        self.selected_style = None 
        self.study = StatsMyData('data.json') 

    def list_menu_options(self) -> List[Tuple[str, Callable]]:
        menu_options = [
            ('Reprocess input data (reads data.json file)', self.study.reprocessFile),
            ('Show top 10 companies hiring graph', self.study.top10CompaniesHiring),
            ('Show top 10 locations hiring graph', self.study.top10LocationsHiring),
            ('Show top 10 positions hiring graph', self.study.top10PositionsHiring),
        ]
        return menu_options

    def prompt_user(self, choices: list[str, Callable], message: str) -> str:
        questions = [
            inquirer.List('selection', message=message, choices=choices),
        ]
        return inquirer.prompt(questions)['selection']
    
    def choose_style(self):
        options = self.list_menu_options()
        final_style_choice = ("Exit",exit)
        options.append(final_style_choice)
        selected_choice = ""
        while (selected_choice != final_style_choice):
            selected_choice = self.prompt_user(options, "What do you wanna do?")
            if selected_choice == final_style_choice:
                print("\nBye!")
                exit()
            else:
                selected_choice()

    def open_menu(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.choose_style()
        a = self.selected_style
        os.system('cls' if os.name == 'nt' else 'clear')
