import config
import dbConnection
from spotify import trackDetails
from lyricsgenius import Genius

mydb = dbConnection.connect()

#####GENIUS CREDENTIAL INFO#####
CLIENT_ID = config.GENIUS_CLIENT_ID

CLIENT_SECRET = config.GENIUS_CLIENT_SECRET

TOKEN = config.GENIUS_TOKEN

genius = Genius(TOKEN)


#####USE OUTPUT FROM SPOTIFY.PY TO LOOP OVER SONGS AND SAVE LYRICS TO DB
for track, artist in trackDetails.items():
  print(type(track), '::', type(artist))
  song = genius.search_song(track, artist)
  # print(song.lyrics)
  # song.save_lyrics()
  #print(len(song.lyrics))
  mycursor = mydb.cursor()
  insert_stmt = (
    "INSERT INTO lyrics (lyrics,trackName,artist) "
    "VALUES (%s,%s,%s)"
  )
  data = (song.lyrics,track,artist)
  mycursor.execute(insert_stmt, data)
  mydb.commit() 
