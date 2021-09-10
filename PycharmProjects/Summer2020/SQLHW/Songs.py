import sqlite3

con = sqlite3.connect("songs.db")
cursor = con.cursor()

cursor.execute("create table if not exists songs (SongName, Artist, Album)")
con.commit()


def add_song(songName, artist, album):
    cursor.execute("insert into songs values(?,?,?)", (songName, artist, album))
    con.commit()
    print("Song added!")

def delete_song(songName):
    cursor.execute("delete from songs where SongName = ?", (songName, ))
    con.commit()
    print("Song deleted!")

def show_songs():
    cursor.execute("select * from songs")
    songList = cursor.fetchall()
    for i in songList:
        print(i)


delete_song("Sail")
show_songs()