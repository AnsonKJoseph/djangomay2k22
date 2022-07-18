import random
import functools

import json
import functools

with open("songs.json", encoding="utf-8") as f:
    data = json.load(f)

    # print(data)

# highest rating song

top_song = max(data, key=lambda s: s["rating"])
print(top_song["rating"])
top_songs = [s for s in data if s["rating"] == top_song["rating"]]
print(top_songs)

# using reduce

t_songs = functools.reduce(lambda s1, s2: s1 if s1["rating"] > s2["rating"] else s2, data)
print(t_songs)

# sad mode songs with random sample of 2


sad_mode = [sad["name"] for sad in data if sad["mode"] == "sad"]
print(sad_mode)

out = random.sample(sad_mode, 2)
print(out)
import random

# total number of songs in album1

# using list comprehension
num_song=[song for song in data if song["album"]=="album1"]
print(len(num_song))

# using filter
album_song_count = list(filter(lambda song: song["album"] == "album1", data))
print(len(album_song_count))

# total number of albums

total_album = set([s["album"] for s in data])
print(len(total_album))

# which album containing most songs

sc = {}
for song in data:
    album_name = song.get("album")  # album1
    if album_name in sc:
        sc[album_name] += 1
    else:
        sc[album_name] = 1
print(sc)

print(max(sc.items(), key=lambda s: s[1]))
