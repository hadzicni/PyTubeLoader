from pytube import YouTube

def download_video(url, file_format):
    try:
        yt = YouTube(url)
        if file_format == 'mp3':
            stream = yt.streams.filter(only_audio=True).first()
        else:
            stream = yt.streams.get_highest_resolution()
        
        if file_format == 'wav':
            stream.download(output_path='downloads', filename='temp_video')
            print('Das Video wurde heruntergeladen und in WAV konvertiert.')
        else:
            stream.download(output_path='downloads')
            print('Video wurde heruntergeladen!')
    except Exception as e:
        print(f"Fehler beim Herunterladen des Videos: {str(e)}")

url = input("Bitte gib die URL des YouTube-Videos ein, das du herunterladen möchtest: ")
file_format = input("Welches Dateiformat möchtest du herunterladen? (mp3/mp4/wav): ").lower()

if file_format not in ['mp3', 'mp4', 'wav']:
    print("Ungültiges Dateiformat! Bitte wähle mp3, mp4 oder wav.")
else:
    download_video(url, file_format)
