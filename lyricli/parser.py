from bs4 import BeautifulSoup as bs4
from lyricli.exceptions import ParserException

class Parser:
    def feed(self, html):
        if(html.status_code == 200):
            html = html.text
            soup = bs4(html, "lxml")
            try:
                songId = soup.find("div", attrs={"class":"section_song"}).find_all("td")[0].find("input")['value']
            except AttributeError:
                raise ParserException(808)
                
        else:
            raise ParserException(html.status_code)

        return songId

    def feed_tab(self, html):
        if(html.status_code == 200):
            html = html.text
            time_table = {}
            soup = bs4(html, "lxml")
            lyrics = soup.find("div", attrs={"class": "lyric"})
            if lyrics:
                for c, i in enumerate(lyrics.strings):
                    time_table[i.strip()] = c
            else:
                raise ParserException(800)
        else:
            ParserException("Status Code", html.status_code)

        return time_table