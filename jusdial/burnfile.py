import csv
import os
class burn:
    def __init__(self):
        pass

    def make_csv_file(self,row,file):

        with open(file,'a') as fl:
            data=csv.writer(fl)
            data.writerow(row)