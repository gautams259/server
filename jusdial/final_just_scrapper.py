import bs4
from collections import defaultdict
import csv
import requests
import re
import os
from burnfile import burn
h={
       'Host':'www.justdial.com',
       'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0',
       'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Language':'en-US,en;q=0.5',
       'Accept-Encoding':'gzip, deflate, br',
       'Referer':'https://www.justdial.com/',
       'Connection':'keep-alive',
       'Cookie':'ppc=; PHPSESSID=8o9ehm971ovtknqoqdk0rsu3e4; TKY=cfbef2509e130c7852073ca44ad656c2856f8175e6c1e65fc00bc107a4cfc942; _ctk=ac78010e22ad26d5fe1b116f5cd6cb0a7a53038f76a4d68f45ab16cf987b6440; main_city=Chennai; attn_user=logout; ppc=; ak_bmsc=65C3FA517878839D606D6A5F9E36038817CD765F4A2600007AA2F35CC124F759~plUBv0MZ4FL5CaQ82TF7lxHlI5ZALcfJTnBgKKJRQNMT0D4dzsBxOuTzpJeLLNur6m2GM0LwurSdfR4oRwlmvGLSdHMwGBZr5r436/vPQ9UkFcgHcjyRtFIcbtJOzVZJiwzc1K53KS9Kzw3bwCrCmeVHjkUU/J3Rc1oaADzVaG77zkALCyGkaVb15yaV1/EaU6V0n+mPVEeBxrRxhZUuosNWIBHx+whBRpZbdLRxS1pmB1QN2xtxbCeKYpRj0OXqHB; scity=Chennai; usrcity=Chennai; inweb_city=Chennai; dealBackCity=Chennai; _ga=GA1.2.1109295841.1559470717; _gid=GA1.2.1043023454.1559470717; _fbp=fb.1.1559470717359.1081048700; RT="sl=2&ss=1559474231628&tt=15750&obo=0&bcn=%2F%2F60062f0c.akstat.io%2F&sh=1559475273633%3D2%3A0%3A15750%2C1559475265456%3D1%3A0%3A11766&dm=justdial.com&si=fe381a22-1a99-4f2d-811c-f6af73bb2ae8&ld=1559475273633&r=https%3A%2F%2Fwww.justdial.com%2FChennai%2FB-Tech-Colleges%2Fnct-11181168&ul=1559475404567"; bm_sv=FC76E7B2CA7E11A5D1AFE160C8BB3D6B~phfBbH9yOpfFPVuN61+7RvQmgl45qpG+DFshjfdK4OmZUwwUsVEThkAbu80dnDQRZneAcmqrkujcOniETHfGXj+AJ8Fw9H/1FQsbc2XhzsOIYMRJLzsD0wZW+z0lb9nlz7LrItflvyCcvcK5rpVs8uV1NprwELOlpuBj5KDX9MM=; akcty=Chennai; inweb_what=B+Tech+Colleges; profbd=0; bdcheck=1; tab=toprs; BDprofile=1; prevcatid=11181168; bd_inputs=7|6|B%20Tech%20Colleges; view=lst_v',
       'Upgrade-Insecure-Requests':'1',
       'Cache-Control':'max-age=0'}
class justdial:
   def __init__(self):
       pass;

   def get_soup(self,url):
       
       soup=bs4.BeautifulSoup(requests.get(url,headers=h).text,'html.parser')
       #print(soup.prettify())
       self.s=soup
       return soup

   def card_link(self):
        arr=[]
        span=self.s.findAll('span',attrs={'class':'jcn'})
        for i in span:
            arr.append(i.find('a').get('href'))
        return arr

   def generate_mob(self,l):
        pattern={
            'icon-lk':'0',
            'icon-yz':'1',
            'icon-dc':'2',
            'icon-vu':'3',
            'icon-ikj':'4',
            'icon-rq':'5',
            'icon-nm':'6',
            'icon-nlm':'7',
            'icon-wyx':'8',
            'icon-ji':'9',
            'icon-hg':')',
            'icon-fe':'(',
            'icon-ba':'-',
            'icon-po':'+'
        }
        s=''
        return pattern.get(l)
        

            
class get_basic_details:
    def __init__(self):
        pass
    def rating(self,soup):
        span=soup.find('span',attrs={'class':'rating'})
        s=span.find('span',attrs={'class':'value-titles'})
        return s.text

    def company(self,soup):
        c=soup.find('div',attrs={'class':'col-sm-9 col-xs-12'})
        company=c.find('span',attrs={'class':'fn'})
        return company.text

    def address(self,soup):
        span=soup.findAll('span',attrs={'class':'adrstxtr'})
        for i in span:
            ad=i.text
            address=ad.replace('(Map)','').strip()
        #print(address)
        return address

    def generate_mob(self,l):
        pattern={
            'icon-lk':'0',
            'icon-ts':'0',
            'icon-wyx':'0',
            'icon-yz':'1',
            'icon-fde':'1',
            'icon-dc':'2',
            'icon-vu':'3',
            'icon-ikj':'0',
            'icon-ji':'4',
            'icon-dc':'4',
            'icon-rq':'5',
            'icon-acb':'5',
            'icon-nm':'6',
            'icon-nlm':'7',
            'icon-wyx':'8',
            'icon-ji':'9',
            'icon-hg':')',
            'icon-fe':'(',
            'icon-ba':'-',
            'comp-icon':'mob '
        }
        
    def mobile(self,soup):
        try:
            c=' '
            a=soup.find('a',attrs={'class':'tel ttel'})
            #for i in a:
            s=a.findAll('span')
            
            for j in s:
                b=j.get('class')
                m=b[1]
                    #print(m)
                mob=str(justdial.generate_mob(self,m))
                c=c+mob
            print(c)
            c=''
                

        except Exception as e:
            print(e)
    def website(self,soup):
        try:
            e=''
            span=soup.findAll('span',attrs={'class':'mreinfp comp-text'})
            for i in span:
                email=i.find('a')
                em=email.get('href')
                if not em:
                    pass
                else : 
                    e=e+em+','
            return e
            
        except Exception as e:
            pass
        

class fetch_data(justdial,get_basic_details):
    
    def __init__(self,url):
        self.url=url
        self.soup=justdial.get_soup(self,url)

    @classmethod
    def fetch(cls,url):
        return cls(url)

    def get_all_data(self):
     try:
         link=justdial.card_link(self)
         arr=[]
         row1=['COMPANY','ADDRESS','RATINGS','SITE']
         
         for i in link:
            soup=justdial.get_soup(self,i)
            c=get_basic_details.company(self,soup)
            print(c)
            #print('\n')
            address=get_basic_details.address(self,soup)
           
            #dd[c].append(address)
            web=get_basic_details.website(self,soup)
            #print(web)
            #print('\n')
            r=get_basic_details.rating(self,soup)

            row=[c,address,r,web]
            b=burn()
            b.make_csv_file(row,'just.csv')
            del row
        
     except Exception as e:
            print(e)
            
class get10class(fetch_data):
    def __init__(self):
        pass;

    def get10all(self,url):
        try:
            #s=justdial.get_soup(url)
            soup=bs4.BeautifulSoup(requests.get(url,headers=h).text,'html.parser')
            ob=fetch_data.fetch(url)
            ob.get_all_data()

            page=soup.findAll('div',attrs={'class':'jpag'})
            
            ar=[]
            for i in page:
                a=i.find_all('a')
                ar.append(a)
            c=ar[0][1:-1]
            for i in c:
                
                ob=fetch_data.fetch(i.get('href'))
                ob.get_all_data()
                
        except Exception as e:
            print(e)


#url='https://www.justdial.com/Chennai/B-Tech-Colleges/nct-11181168'
url='https://www.justdial.com/Bangalore/Software-Companies/nct-10443565'
ob=fetch_data(url)
#ob.get_all_data()
g=get10class()
g.get10all(url)
