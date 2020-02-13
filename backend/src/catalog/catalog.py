import csv 
import os
import random

from lyrics.noplpsong import NoPLPSong

from lib.logger import get_logger
logger = get_logger(LOG_NAME='noplp')

class Catalog(object):
    def __init__(self, list_filepath):
        super(Catalog, self).__init__()

        self.SONG_PATH = os.path.abspath(os.path.join(list_filepath, os.pardir))

        self.list_filepath = list_filepath
        self.songs = []

        self.artists_index = {}
        self.title_index = {}
        self.category_index = {}
        self.same_song_index = []

        logger.debug("Loading list...")
        self._load_list()

    def _load_list(self):
        with open(self.list_filepath, 'r', encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';', quoting=csv.QUOTE_NONE)
            for row in reader:
                logger.debug(dict(row))
                song = NoPLPSong(row['Title'], row['Artist'], row['Decade'], self.SONG_PATH)

                if song.get_artist() not in self.artists_index:
                    self.artists_index[song.get_artist()] = []
                self.artists_index[song.get_artist()].append(song)

                if row['Title'] not in self.title_index:
                    self.title_index[row['Title']] = []
                self.title_index[row['Title']].append(song)

                themes = row["Themes"].split(',')
                for t in themes:
                    if t not in self.category_index:
                        self.category_index[t] = []
                    self.category_index[t].append(song)

                if row['Final'] == "MC":
                    self.same_song_index.append(song)

    def get_categories(self, n, seen_categories):
        categories = list(self.category_index.keys())
        shuffle = random.sample(categories, len(categories))

        cat_to_return = []
        for c in shuffle:
            if len(cat_to_return) == n:
                break
            if c in seen_categories:
                continue
            cat_to_return.append(c)

        return cat_to_return

    def get_songs_from_category(self, category):
        n_songs = 2
        songs = self.category_index[category]
        if n_songs > len(songs):
            return songs
        return list(map(lambda x: songs[x], random.sample(range(0, len(songs)), n_songs)))

    def get_song(self, artist, title):
        artist_songs = self.artists_index[artist]
        for s in artist_songs:
            if s.title == title:
                return s

        return None