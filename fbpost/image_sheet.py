from collections import defaultdict
from oauth2client.service_account import ServiceAccountCredentials
from oauth2client import file, client, tools
import gspread
from datetime import datetime


SCOPES = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
store = file.Storage('token.json')
credentials = store.get()
if not credentials or credentials.invalid:
    flow = client.flow_from_clientsecrets('client.json', SCOPES)
    credentials = tools.run_flow(flow, store)

service = gspread.authorize(credentials)
sheet=service.open('image_data').sheet1

def mark_cell_as_published(c):
    sheet.update_acell('c'+str(c), 'done')
    sheet.update_acell('d'+str(c),datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

def get_images():
    image_exist=True
    c=2
    up_data=[]
    while image_exist:
        l=sheet.row_values(c)
        #print(len(l))
        if  l:
            if  len(l)>=3:
                if l[2]:
                    if l[2] =='done':
                        print("{} is published".format(l)) 
                        print("moving for next line")
                        c=c+1
                    else:
                        print("please donot write anything in PUBLISH INFORMATION this column shoud contain system generated string",l)
                        print("please check {} column".format(c))
                        image_exist=False
                else:
                    print("{} is not published we are going to publish to group".format(l)) 
                    image_exist=False 
                    up_data=l[0:2]
                    up_data.append(c)
                    c=c+1      
                    return up_data
            else:
                print("{} is not published we are going to publish to group".format(l)) 
                image_exist=False 
                up_data=l[0:2]
                up_data.append(c)
                c=c+1
                return up_data         
        else:
            print("no images found in google sheet or any row is vecant...")
            image_exist=False


def main():
    c=get_images()
    print('executing')
    print(c)

if __name__ == '__main__':
    main();
  