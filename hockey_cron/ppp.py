from bs4 import BeautifulSoup as bs
import requests
import arrow

def make_soup(url):
    soup=bs(requests.get(url).text,'html.parser')
    return soup

def get_match(t_id):
    games=[]
    soup=make_soup("https://tms.fih.ch/competitions/"+t_id+str('/matches'))
    [tbody]=soup.select('tbody')
    tr=tbody.select('tr')
    for i in tr:
        row={}
        td=i.select('td')
        l=td[2].find('a')
        title=l.text
        game_link=l.get('href')
        span=td[1].select('span')
        mt=span[0].get('data-datetimelocal__notimechange')
        timezone=span[0].get('data-timezone')
        matchtime=arrow.get(mt).replace(tzinfo=timezone).to('utc').isoformat()
        #print(title,game_link,matchtime,t_id)
        games+=[{'Title':title,'Game_link':game_link,'Matchtime':matchtime,'Tournament_id':t_id}]
    return games

def get_tournament(url):
    soup=make_soup(url)
    [tbody]=soup.select('tbody')
    tr=tbody.select('tr')
    for i in tr:
        td=i.select('td')
        l=td[1].find('a')
        link=l.get('href')
        tournament=l.text
        tournament_date=td[2].text.strip()
        print(link,tournament,tournament_date)
        tournament_id=link.split('/')[4]
        games=get_match(tournament_id)
        print(games)
        

def main():
    url='https://tms.fih.ch/competitions?view=upcoming'
    get_tournament(url)

if __name__=='__main__':
    main()