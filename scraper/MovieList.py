from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re

class MovieList:
    def __init__(self, info):
        self.url = info['url']
        self.query = info['query']
        self.pattern = info['pattern']

    def get_soup(self):
        # set known browser user agent
        r = Request(self.url, headers={'User-Agent': 'Mozilla/5.0'})
        content = urlopen(r).read()
        soup = BeautifulSoup(content, 'html.parser')
        return soup

    def fetch_list(self):
        res = self.get_soup()
        return list(map(lambda x: x.text.replace(u'\xa0', u' '), res.select(self.query)))

    def parse_movie(self, s):
        match = re.search(self.pattern, s)
        if match:
            m = match
            return {'rank': m.group(1), 'title': m.group(2), 'year': m.group(3)}
        return None

    def parse_movies(self):
        parsed_movies = []
        for movie in self.fetch_list():
            parsed_movie = self.parse_movie(movie)
            if parsed_movie != None:
                parsed_movies.append(self.parse_movie(movie))
        return parsed_movies