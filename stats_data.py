import pandas as pd
import matplotlib.pyplot as plt
import json
from collections import defaultdict

class StatsMyData:
    def __init__(self, jsonfileName):
        self.data = pd.read_json(jsonfileName) 
        self.sourceFileName = jsonfileName       

    def output(self):
        print(self.data)

    def summarize(self):
        print(self.data.describe())

    def reprocessFile(self):
        self.__init__(self.sourceFileName)

    def filterByCompany(self, company):
        results = self.data[self.data['company'] == company]
        print(results)

    def showTopCompanies(self):
        sorted = self.data.sort_values(by='company', ascending=False)
        print(sorted)

    def top10CompaniesHiring(self):
        job_offer_by_company = self.data['company'].value_counts().head(10)#top 10
        job_offer_by_company.plot(kind='barh', title='Testing')
        plt.ylabel('Company')
        plt.xlabel('Offer job count')
        plt.show()


    def top10PositionsHiring(self):
        jobs_title_by_company = self.data['job_title'].value_counts().head(10)#top 10
        jobs_title_by_company.plot(kind='barh', title='Testing')
        plt.ylabel('Job Title')
        plt.xlabel('Offer job count')
        plt.show()


    def top10LocationsHiring(self):
        job_location_count = self.data['job_location'].value_counts().head(10)#top 10
        job_location_count.plot(kind='barh', title='Testing')
        plt.ylabel('Job Location')
        plt.xlabel('Offer job count')
        plt.show()

    def read_file(self):
        with open(self.json_file, 'r') as file:
            self.data = json.load(file)
    
    
