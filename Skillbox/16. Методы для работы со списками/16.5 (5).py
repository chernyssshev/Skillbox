violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

song_count = int(input("Сколько песен выбрать? "))
song_time = float(0)

for song in range(song_count):
    print(f"Название {song + 1} песни:", end = " ")
    song = input("")
    for songs in range(len(violator_songs)):
        if song == violator_songs[songs][0]:
            song_time += round(violator_songs[songs][1], 2)

print("Общее время звучания песен: ", song_time)
