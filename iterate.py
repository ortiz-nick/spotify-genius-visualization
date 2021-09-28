import dbConnection
import string 

mydb = dbConnection.connect()

mycursor = mydb.cursor()

mycursor.execute("SELECT lyrics, artist, trackName  FROM lyrics")

allData = mycursor.fetchall()

lyricList = []

# print(allData[0][0])

for data in allData:
	# track_dictionary = {}
	# track_dictionary["lyrics"] = allData[0]
	# track_dictionary["artist"] = lyric[1]
	# track_dictionary["trackName"] = lyric[2]
	# track_info_list.append(track_dictionary)
	lyricList.append(data[0])
	# print(data["lyrics"])

# start cleaning data
for lyrics in lyricList:
	#delete all punctuation
	lyrics = lyrics.translate(str.maketrans('', '', string.punctuation))
	print(lyrics)



###Get instances of words used multiple times