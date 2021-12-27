import pytest

import os
import sys

from driver import spotify

class TestSpotify:
    def test_init(self, client_id, client_secret):
        driver = spotify.SpotifyDriver(client_id, client_secret)
        assert driver.client_id == client_id
        assert driver.client_secret == client_secret

    def test_login(self, client_id, client_secret):
        driver = spotify.SpotifyDriver(client_id, client_secret)
        assert driver.token

    def test_search(self, client_id, client_secret):
        driver = spotify.SpotifyDriver(client_id, client_secret)
        track = driver.search("Yellow Submarine", "The Beatles")
        assert track