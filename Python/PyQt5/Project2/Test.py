from moviepy import VideoFileClip

# Chemin du fichier MP4
video = VideoFileClip("MP4\\Uzishettan - LIYEM (EXCLUSIVE Lyric Clip) [Prod By Novi].mp4")

# Extraire l'audio et sauver en MP3
video.audio.write_audiofile("MP3\\Uzishettan - LIYEM (EXCLUSIVE Lyric Clip) [Prod By Novi].mp3")
