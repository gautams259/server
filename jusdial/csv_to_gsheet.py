import csv
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
sheets = service.open('data').sheet1

def add_header():
    sheets.update_acell('A1','COMPANY')
    sheets.update_acell('B1','Address')
    sheets.update_acell('C1','Rating')
    sheets.update_acell('D1','web')
    sheets.update_acell('E1','MOB')

def upload_to_google_sheet(l):
    c=2;
    for i in l:
        sheets.update_acell('A'+str(c),i[0])
        sheets.update_acell('B'+str(c),i[1])
        sheets.update_acell('C'+str(c),i[2])
        sheets.update_acell('D'+str(c),i[3])
        sheets.update_acell('E'+str(c),i[4])
        c=c+1
        
    
    
for i in sheets.range('A1:C1'):
    print(i)

def make_list_from_dic(fl):
    ar=[]
    with open(fl) as csv_file:
        csvreader=csv.reader(csv_file,delimiter=',')
        for i in csvreader:
            ar.append(i)
    return ar

if __name__ =='__main__':
    l=make_list_from_dic('just.csv')
    #for i in l:
    #    print(i)
    add_header()
    upload_to_google_sheet(l)
