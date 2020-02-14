from random import randint
import uuid
import os
import re

from lib.utils import mask_line

from lib.logger import get_logger
logger = get_logger(LOG_NAME='noplp')

class NoPLPSong(object):
    def __init__(self, title, artist, decade, basepath, tab):
        super(NoPLPSong, self).__init__()

        self.id = self.id = uuid.uuid1().hex
        self.title = title
        self.artist = artist
        self.decade = decade
        self.basepath = basepath
        self.tab = tab

        self.current_load_level = None

        self.lines = []
        self.levels = {} # {"50": [...], "40": [...] }

        self.load_song()

    def __str__(self):
        return "{0} - {1}".format(self.title, self.artist)

    def __repr__(self):
        return self.__str__()

    def get_filename(self):
        return "{}.txt".format(self.title.replace("'", "_"))

    def get_artist_dirname(self):
        m = self.artist.split(',')
        if len(m) > 1:
            return m[0].replace("'", "_")
        return self.artist.replace("'", "_")

    def get_artist(self):
        m = self.artist.split(',')
        if len(m) > 1:
            return m[1]
        return m[0]

    def get_filepath(self):
        return os.path.join(os.path.join(self.basepath, self.get_artist_dirname()), self.get_filename())

    def load_song(self):
        # logger.info("Loading song...")
        # logger.info(self.get_filepath())

        regex = r"<(\d+)>"

        with open(self.get_filepath(), 'r', newline=None, encoding='utf-8-sig') as f:
            for line in f.readlines():
                line = line.strip()
                match = re.match(regex, line)
                if match:
                    self.current_load_level = match.group(1)
                    self.levels[self.current_load_level] = []
                else:
                    if not self.current_load_level:
                        self.lines.append(line)
                    else:
                        self.levels[self.current_load_level].append(line)

    def generate_song(self, level):
        logger.info("Generating song for {0} - {1}, level {2}".format(self.title, self.artist, level))
        
        if level not in self.levels:
            logger.error("Level {0} doesn't exist".format(level))
            return []

        missing_lyrics = self.levels[level][randint(0, len(self.levels[level])-1)]

        lines_to_return = []
        for i in range(len(self.lines)):
            line = self.lines[i]
            if missing_lyrics in line:
                s = line.split(missing_lyrics)
                lines_to_return.append(s[0])
                lines_to_return.append(mask_line(missing_lyrics))

                logger.debug("Line: {}".format(line))
                logger.debug("maskline: {}".format(mask_line(missing_lyrics)))
                logger.debug("words: {}".format(line.split(' ')))
                logger.debug("len words: {}".format(len(line.split(' '))))
                logger.debug("range: {}".format(range(len(line.split(' ')))))
                
                return lines_to_return, missing_lyrics
            else:
                # Check if it spans over mutliple lines
                if i != 0:
                    joined_lines = ' '.join([self.lines[i-1], self.lines[i]])
                    if missing_lyrics in joined_lines:
                        lines_to_return.pop()
                        s = joined_lines.split(missing_lyrics)
                        lines_to_return.append(s[0])
                        lines_to_return.append(mask_line(missing_lyrics))
                        return lines_to_return, missing_lyrics
                    else:
                        lines_to_return.append(line)
                else:
                    lines_to_return.append(line)

        return lines_to_return, missing_lyrics

