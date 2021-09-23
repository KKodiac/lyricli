"""
    멜론 API에 접속합니다.
"""

import requests

from lyricli.exceptions import ConsoleException, ParserException
from lyricli.output import print_out
from lyricli.parser import Parser

BASE_URL = "https://www.melon.com/"
INDEX_POSTFIX = "search/total/index.htm?q="
DETAIL_POSTFIX = "song/detail.htm?songId="

def get_lyrics(args):
    title = "+".join(args.title.split())
    artist = args.artist if args.artist else ""
    artist = "+".join(artist.split())
    query_string = "{}+{}".format(title, artist)
    url = '{}{}{}'.format(BASE_URL, INDEX_POSTFIX, query_string)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'
        }
    html = requests.get(url, headers=headers)

    parser = Parser()
    songId = parser.feed(html)
    tab_url = '{}{}{}'.format(BASE_URL, DETAIL_POSTFIX, songId)
    html_tab = requests.get(tab_url, headers=headers)
    lyric_table = parser.feed_tab(html_tab)
    for i in lyric_table:
        print_out("<blue>{}</blue>".format(i))
    
    return lyric_table

