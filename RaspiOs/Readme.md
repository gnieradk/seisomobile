# Raspberry Pi Operating System
The Raspberry Pi operating system image is placed in Google drive folder:

https://drive.google.com/drive/folders/1xXPh7sKkLgpkb66E9XRqQ87OLExOKXbF?usp=sharing

The original image of Raspberry system is prepared for 32GB capacity SD card. But I haven't been able to find any place where I would be able to put a file of this size. So I used [PiShrink](https://gfile:///media/gregosh/Storage/seisomobile/seismoweb/Readme.md
ithub.com/Drewsif/PiShrink) script in order to reduce the file size. The current size is about 2GB. I haven't tried yet, but probably it could be written into some SD card and the system should boot from thi card.

The system which is installed is the newest image based on Debian Buster [Raspberry OS](https://www.raspberrypi.org/downloads/raspberry-pi-os/).

In the image the ROS in branch [Noetic Ninjemys](https://www.raspberrypi.org/downloads/raspberry-pi-os/) is installed. 

For video streaming the tests of using ROS module [raspicam_node](https://www.raspberrypi.org/downloads/raspberry-pi-os/) has been done. But there were present a significant transmission dealys (lags) in streaming video to web browser .

So at this moment the [uv4l-server](https://www.linux-projects.org/uv4l/tutorials/streaming-server/) is intalled and used for video streaming. The video streaming server is installed as a typical linux service which is started during booting and starts automatically. Using this video streaming the lags are not present in streamed video. Only for visualisation purpose is convinient solution at this moment.
