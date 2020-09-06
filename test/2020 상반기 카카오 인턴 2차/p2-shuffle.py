# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import codecs
import random
from pprint import pprint
sys.stdin = codecs.getreader("utf-8")(sys.stdin.detach())
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

def Fisher_Yates_shuffle(arr):
    copied = arr[:]
    for i in range(len(copied)-1,0,-1):
        j = random.randrange(0, i+1)
        copied[i], copied[j] = copied[j], copied[i]
    return copied

def dither(songs):


T = int(input())
for _ in range(T):
    playlist = input().split('\t')
    artist = input().split('\t')
    n = len(set(artist))
    m = len(playlist)
    board = [[0]*m for _ in range(n)]
    pairs = list(zip(artist, playlist, [i for i in range(m)]))
    # first shuffling
    shuffled_pairs = Fisher_Yates_shuffle(pairs)
    # print(*shuffled_pairs, sep='\n')
    d = {}
    for artist, song, song_id in shuffled_pairs:
        if artist not in d:
            d[artist] = [0] * m
        else:
            d[artist][song_id] = 1
    pprint(d)
    for songs, artist in d.items():

    # print(shuffled_playlist)
    # print(shuffled_artist)
    print("\t".join([song for _, song, _ in shuffled_pairs]))
