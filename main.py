from pytube import YouTube
import ffmpeg

# Normal download function
""" def download(link, video_name):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download(filename=f'{video_name}.mp4')
        print("Download is completed successfully")
    except:
        print("An error has occurred") """

# Download function with audio and video merging (more quality)
def download_high_quality(url, video_name):
    yt = YouTube(url)
    video = yt.streams.filter(adaptive=True).filter(mime_type='video/webm').first()

    try:
        video.download()
        print("Download video is completed successfully")
    except:
        print("An error has ocurred during video download")
    
    audio = yt.streams.filter(only_audio=True).first()
    try:
        audio.download()
        print("Download audio is completed successfully")
    except:
        print("An error has ocurred during audio download")

    print("Merging audio and video")
    
    try:
        video_file = video.get_file_path()
        audio_file = audio.get_file_path()

        audio_stream = ffmpeg.input(audio_file).audio
        print("----Audio stream found----")
        video_stream = ffmpeg.input(video_file).video
        print("----Video stream found----")

        output_stream = ffmpeg.output(audio_stream, video_stream, f'./{video_name}.webm', vcodec='copy', acodec='libvorbis')
        print("----Output stream created----")
        
        ffmpeg.run(output_stream)
        print("Merging is completed successfully")
    except:
        print("An error has ocurred during merging")

def main():
    link = input("Enter the YouTube video URL: ")
    video_name = input("Enter the video name: ")

    download_high_quality(link, video_name)
    # download(link, video_name) # Normal download function 

if __name__ == "__main__":
    main()