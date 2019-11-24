echo 'Hello! Starting now...'
echo 'Make sure you downloaded into the Downloads/ folder'
sleep 3
echo 'Now, can you please enter your password?'
sudo apt install curl
sudo apt install python3
sudo apt install youtube-dl
sudo apt install ffmpeg
cd $HOME/Downloads/
mv 'YouTube Downloader Linux'/'YouTube Downloader.desktop' $HOME/Desktop/
mv 'YouTube Downloader Linux' $HOME/
cd $HOME/Desktop/
chmod +x 'YouTube Downloader.desktop'
echo 'Nice! Now you can just double-click the launcher called Youtube Downloader in your desktop'
rm Launcher.sh
exit
