import csv
import os
from collections import defaultdict
from oauth2client.service_account import ServiceAccountCredentials
from oauth2client import file, client, tools
import gspread

SCOPES = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
store = file.Storage('token.json')
credentials = store.get()
if not credentials or credentials.invalid:
    flow = client.flow_from_clientsecrets('client.json', SCOPES)
    credentials = tools.run_flow(flow, store)

service = gspread.authorize(credentials)
sheet=service.open('data').sheet1

def write_to_gsheet(l):
    sheet.update_acell('A1','Company')
    sheet.update_acell('B1','Address')
    sheet.update_acell('C1','Rating')
    sheet.update_acell('D1','Web')
    sheet.update_acell('D1','Mob')
class burn:
    def __init__(self):
        self.data=defaultdict()
        pass

    def make_csv_file(self,row,file):

        with open(file,'a') as fl:
            data=csv.writer(fl)
            data.writerow(row)


    def makedict(self,company,address,r,web,mob):
        
        if not self.data.get(company):
            self.data[company]=[]
        self.data[company].append(address)
        #print(address)
        self.data[company].append(r)
        self.data[company].append(web)
        self.data[company].append(mob)
        return self.data
       

    def get_dict(self):
        return self.data
