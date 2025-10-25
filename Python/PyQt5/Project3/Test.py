from moviepy import VideoFileClip

# Chemin du fichier MP4
video = VideoFileClip("downloads\\Inkonnu - MORAL feat. NOUVO (Prod.By NOUVO) [Arabi Album].mp4")

# Extraire l'audio et sauver en MP3
video.audio.write_audiofile("Imge\\Inkonnu - MORAL feat. NOUVO (Prod.By NOUVO) [Arabi Album].mp3")
