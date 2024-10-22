import json
import os
import threading
import inquirer
from collections import defaultdict
from stats_data import StatsMyData
from typing import Dict, List, Tuple, Callable
from functools import partial

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
            ('View jobs offer by company', self.list_jobs_options),
        ]
        return menu_options

    def print_out(self, iteems):
        print(iteems[['job_title','job_location','link']])

    def list_jobs_options(self) -> List[Tuple[str, Callable]]:
        companies = self.study.getCompanies()
        submenu_options = []
        for company in companies:            
            my_tuple = (f'{company[0]} - Count({len(company[1])})', partial(self.print_out, iteems= company[1]))            
            submenu_options.append(my_tuple)
        submenu_action = self.prompt_user(submenu_options, "pick up a company")
        submenu_action()

    def prompt_user(self, choices: list[str, Callable], message: str) -> str:
        questions = [
            inquirer.List('selection', message=message, choices=choices),
        ]
        return inquirer.prompt(questions)['selection']
    
    def choose_action(self, options):
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
        self.choose_action(self.list_menu_options())
        a = self.selected_style
        os.system('cls' if os.name == 'nt' else 'clear')
