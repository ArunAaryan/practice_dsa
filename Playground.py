def printCurrentSong(distance, speed, songDuration):
	time_in_minutes = distance / speed
	current_song = 0
	for idx, song in enumerate(songDuration):
		current_song += 1
		minutes = int(song.split(':')[0])
		seconds = int(song.split(":")[1])
		t_seconds = (minutes * 60) + seconds
		time_in_minutes -= t_seconds 
		if time_in_minutes <= 0:
			print (current_song)
	print( current_song)

res = printCurrentSong(2000, 5, ['05:30', '02:04']) 
print(res)


