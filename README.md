# High-Quality YouTube downloader

## Description
This project is a Python script that allows you to download YouTube videos in high quality, merging the video and audio into a single file.

It uses the `pytube` library to download the content and `ffmpeg` to merge the video and audio files.

## Requirements
Before running the script, make sure you have the following dependencies installed:

- Python 3.x
- `pytube`
- `ffmpeg`

You can install them using `pip`:
```
pip install pytube ffmpeg-python
```

Additionally, you must have `ffmpeg` installed on your system. You can download and install it from [here](https://ffmpeg.org/download.html).

## Usage
To use the script, follow these steps:

1. Clone this repository or download the `main.py` file.
2. Open a terminal in the directory where the `main.py` file is located.
3. Run the script with the following command:
```
python main.py
```
4. Enter the YouTube video URL when prompted.
5. Enter the name you want to give to the downloaded file (without the extension).

The script will download the video and audio separately, then merge them into a `.webm` file.

## Example execution
```sh
$ python main.py
Select an option
        1. Normal download (mp4 format)
        2. High quality download (webm format)

Enter the number of the option: 2
Enter the YouTube video URL: https://www.youtube.com/watch?v=dQw4w9WgXcQ
Enter the video name: example
Select the resolution
        1. 144p
        2. 240p
        3. 360p
        4. 480p
        5. 720p
        6. 1080p

Enter the number of the option: 5
Download video is completed successfully
Download audio is completed successfully
Merging audio and video
----Audio stream found----
----Video stream found----
----Output stream created----
[...]
Merging is completed successfully
```

## Example comparison
Below are example images to demonstrate the difference in video quality:

#### Low-Quality Video Capture
![Figure 1: Capture from a low-quality video.](./normal-download-image.jpg)

#### High-Quality Video Capture
![Figure 2: Capture from the same video but in high quality using this script.](high-quality-download-image.jpg)

These images highlight the significant improvement in video quality that can be achieved by using the high-quality download feature of this script.

## Notes
- Make sure you have enough disk space for the downloaded video and audio files, as well as the final merged file.
- If you encounter any issues during the download or merging process, ensure you have the latest versions of `pytube` and `ffmpeg` installed.

## Contributions
If you would like to contribute to this project, you can do so in the following ways:
- Reporting bugs
- Suggesting improvements
- Submitting pull requests with enhancements or fixes

## TODO
- Remove useless files created during download and merging
- Improve error handling and user feedback
- Improve cli interface 