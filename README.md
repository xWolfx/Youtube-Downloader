# Youtube-Downloader
Script to download Youtube videos using youtube-dl in an easy way. This is the linux version.

Windows version coming *soon*.

The App will download the highest quality video available.

## Dependencies
You will need to have [youtube-dl](https://github.com/ytdl-org/youtube-dl) installed.

From their README:

To install it right away for all UNIX users (Linux, macOS, etc.), type:

```
sudo curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl
sudo chmod a+rx /usr/local/bin/youtube-dl
```

If you do not have curl, you can alternatively use a recent wget:

```
sudo wget https://yt-dl.org/downloads/latest/youtube-dl -O /usr/local/bin/youtube-dl
sudo chmod a+rx /usr/local/bin/youtube-dl
```

If you want the automatic postprocessor to transform your video to .mp4, you will need to have [ffmpeg](https://github.com/FFmpeg/FFmpeg) or [avconv](https://github.com/libav/libav) installed.

On Debian based distributions, you can simply paste:

```
sudo apt install ffmpeg
```

## Usage
If the script is in your home folder. Simply open your terminal and paste:

```
python3 YouTube-Script.py
```

Then follow the instructions.



A more easy-to-use version will come *soon*.
