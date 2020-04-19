import argparse
from dotenv import find_dotenv, load_dotenv
import json
import lyricsgenius as lg
import os
from tqdm import tqdm

parser = argparse.ArgumentParser(description='Download songs lyrics for the specific artist.')
parser.add_argument('artist', type=str, help='Artist name. Use apostrophe if needed')
args = parser.parse_args()

load_dotenv(find_dotenv())

CLIENT_ACCESS_TOKEN = os.getenv('CLIENT_ACCESS_TOKEN')

g = lg.Genius(CLIENT_ACCESS_TOKEN)
artist = g.search_artist(args.artist, sort="title")
artist.save_lyrics('.datalyrics.json')

json_file = open('.datalyrics.json').read()
content = json.loads(json_file)
songs = content['songs']

with open('./data/lyrics.txt', 'w') as output_file:
  for song in tqdm(songs):
    if song['lyrics'] is None:
      continue

    output_file.write(song['title'] + '\n')
    output_file.write(song['lyrics'] + '\n')

os.remove('.datalyrics.json')
