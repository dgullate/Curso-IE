# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.2'
#       jupytext_version: 0.8.6
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %%
import lyricsgenius
import pandas as pd

# %%
artist_name = 'Joaquín Sabina'
genius = lyricsgenius.Genius('Fz8_mx7lXTVotUo8yoQ6hljk89x6H1i8Enq8s39aiJO_uGZNl2EaTBG2KaNN0Q-7')
artist = genius.search_artist(artist_name, max_songs=3, sort="title")
print(artist.songs)

# %%


# %%
artist.songs[0].__dict__

# %%
columns = ['author', 'album', 'title', 'lyrics']
df = pd.DataFrame(columns=columns)

# %%
for song in artist.songs:
    author = artist.name
    lyrics = song.lyrics
    title = song.title
    album = song.album
    df = df.append([[author,album,title,lyrics]],columns = co)
#     print(song.lyrics)
    
    break

# %%
df

# %%
song_name = "19 días y 500 noches"
song = genius.search_song(song_name, artist.name)
print(song.lyrics)

# %%


