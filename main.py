from dotenv import load_dotenv

load_dotenv()

import time
import os
import curses

from insta_spotify_status.ascii_song_player_ui import ASCIISongPlayerUI
from insta_spotify_status.spotify_api import SpotifyAPI
from insta_spotify_status.utils import parse_song_data


def main(stdscr: curses.window):
    params = {
        "base_url": os.getenv("SPOTIFY_API_BASE_URL"),
        "email": os.getenv("SPOTIFY_API_EMAIL"),
    }
    spotify_api = SpotifyAPI(**params)

    while True:
        song_data = spotify_api.get_currently_playing()

        if song_data is None:
            ui_text = "No song is currently playing."
        else:
            ui_params = parse_song_data(song_data)
            ui_text = ASCIISongPlayerUI.get_ui(**ui_params)

        stdscr.clear()
        stdscr.addstr(0, 0, ui_text)
        stdscr.refresh()

        time.sleep(1)


if __name__ == "__main__":
    curses.wrapper(main)
