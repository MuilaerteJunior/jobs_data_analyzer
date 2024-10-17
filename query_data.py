import json
from collections import defaultdict

class ProcessData:
    def __init__(self):                
        self.jobs_by_company = defaultdict(list)
        self.jobs_by_location = defaultdict(list)
        self.jobs_by_position = defaultdict(list)

    def set_parameters(self, parameters):
        self.json_file = parameters.get('filename')

    def read_file(self):
        with open(self.json_file, 'r') as file:
            self.data = json.load(file)
    
    def process(self):
        self.read_file()
        # You can also iterate over the array if needed
        for item in self.data:
            print(f"Company: {item['company']}, Job title: {item['job_title']}, Job Location: {item['job_location']}")
            self.jobs_by_company[item['company']].append(item['job_title'])
            self.jobs_by_location[item['job_location']].append(item['job_title'])
            self.jobs_by_position[item['job_title']].append(item['job_location'])
        print('\n')
        
        sorted_jobs_by_company = sorted(self.jobs_by_company.items(), key=lambda item: len(item[1]), reverse=True)
        sorted_jobs_by_location = sorted(self.jobs_by_location.items(), key=lambda item: len(item[1]), reverse=True)
        sorted_jobs_by_position = sorted(self.jobs_by_position.items(), key=lambda item: len(item[1]), reverse=True)
        
        print('\n\nJobs by company\n')
        self.printOut(sorted_jobs_by_company)
        print('\n\nJobs by location\n')
        self.printOut(sorted_jobs_by_location)
        print('\n\nJobs by position\n')
        self.printOut(sorted_jobs_by_position)

        print(f"\n\nTotal {len(self.data)}")
        

    def printOut(self, item):
        for groupKey,children in item:
            print(f"Group Key: {groupKey}")
            print(f"Count: {len(children)}")
            print(f"Items: {children}")
            print('\n')

