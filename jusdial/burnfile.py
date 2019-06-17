import csv
import os
from collections import defaultdict

class burn:
    def __init__(self):
        self.data=defaultdict()
        pass

    def make_csv_file(self,row,file):

        with open(file,'a') as fl:
            data=csv.writer(fl)
            data.writerow(row)

    def makedict(self,company,address,r,web,):
        
        if not self.data.get(company):
            self.data[company]=[]
        self.data[company].append(address)
        #print(address)
        self.data[company].append(r)
        self.data[company].append(web)
        return self.data
       

    def get_dict(self):
        return self.data
