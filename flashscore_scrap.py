import bs4
import requests

class flashscoresoup:
    def __init__(self):
        pass;
    def makesoup(self,url):
        i='https://www.flashscore.com/match/2ieVkiY3/#video'
        h={'Host':'d.flashscore.com',
            'User-Agent':'core',
            'Accept':'*/*',
            'Accept-Language':'*',
            'Accept-Encoding':'gzip,deflate,br',
            'Referer':'https://d.flashscore.com/x/feed/proxy-local',
            'X-GeoIP':'1',
            'X-Referer':i,
            'X-Fsign':'SW9D1eZo',
            'X-Requested-With':'XMLHttpRequest',
            'Connection': 'keep-alive',
            'Cookie':'_ga=GA1.2.149667040.1559363495; _gid=GA1.2.1231578565.1559363495; _sessionhits_UA-207011-5=2; _gat_UA-207011-5=1; _session_UA-207011-5=true',
            'TE':'Trailers'}    
        soup=bs4.BeautifulSoup(requests.get(url,headers=h).text,'html.parser')
        return soup

class flashscorescrapping(flashscoresoup):
    def __init__(self):
        pass
    def fetch_video_url(self,url):
        soup=flashscoresoup.makesoup(self,url)
        self.s=soup
        a=soup.findAll('a')
        link=[]
        for i in a:
            video_link=i.get('href')
            arr=video_link.split('/')
            l='https://vc.sporttube.com/video/2019/6/1/'+arr[4]+".mp4"
            link.append(l)
        
        pl=[]
        strong=soup.findAll('strong')
        for i in strong:
            p=i.text
            player=p.replace('Wicket','')
            pl.append(player)
        
        d=dict(zip(pl,link))
        print(d)
        

    

        

url='https://d.flashscore.com/x/feed/d_hi_KS5QjXIc_en_1'
url='https://d.flashscore.com/x/feed/d_hi_2ieVkiY3_en_1'
ob=flashscorescrapping()
ob.fetch_video_url(url)
#ob.getplayername()
