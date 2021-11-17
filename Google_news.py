from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests

root = "https://www.google.com/"
link = "https://www.google.com/search?q=rohit+sharma&rlz=1C1CHBD_enIN926IN926&tbm=nws&sxsrf=ALeKk00ND6wgXZuyYHLRDZcjz0J3Ej38Qw:1624803047543&source=lnt&tbs=qdr:w&sa=X&ved=2ahUKEwja5-mD_7fxAhXfILcAHRzaDHIQpwV6BAgHECE&biw=1242&bih=597&dpr=1.1"

def news(link):
        req = Request(link, headers = {'User-Agent':'Mozilla/5.0'})
        webpage = urlopen(req).read()
        with requests.Session() as c:
            soup = BeautifulSoup(webpage, 'html5lib')
            for item in soup.find_all('div',  attrs ={'class': 'ZINbbc xpd O9g5cc uUPGi'}):
                raw_link = (item.find('a', href =True)['href'])
                link = (raw_link.split("/url?q=")[1]).split('&sa=U&')[0]
                #print(item)
                title = (item.find('div', attrs={'class': 'BNeawe vvjwJb AP7Wnd'}).get_text())
                description = (item.find('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'}).get_text())

                title = title.replace(",", "")
                description = description.replace(",", "")


                time = description.split(" · ")[0]
                descript = description.split(" · ")[1]
                print(title)
                print(time)
                print(descript)
                print(link)
                document = open("data.csv","a")
                document.write("{}, {}, {}, {} \n".format(title, time, descript, link))
                document.close()

            next = soup.find('a', attrs={'aria-label': 'Next Page'})
            next = print(next['href'])
            link = root + next
            news(link)

news(link)
