from download.download import download, download_high_quality, get_available_resolutions
from terminal.input import show_list_menu

def main():
    index = show_list_menu("Select an option", ["Normal download (mp4 format)", "High quality download (webm format)"])
    link = input("Enter the YouTube video URL: ")
    video_name = input("Enter the video name: ")

    if index == 0:
        download(link, video_name)
    else:
        resolution_options = get_available_resolutions(link)
        index_resolution = show_list_menu("Select the resolution", resolution_options)
        download_high_quality(link, video_name, resolution_options[index_resolution]) 

if __name__ == "__main__":
    main()