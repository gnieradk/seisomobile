#Web application for platform control
The web application for platform control consists of two web pages:

* camera.html
* wheels.html

The file camera is simple and includes only a html tag ```<img>``` which shows the video stream from uv4l-server.

The wheels.html includes front end written in html for basic commands sending to the platform. The commands are sended by into ROS service. For the connection and command sending the [roslibjs](http://wiki.ros.org/roslibjs) is used. The javascript code is written directly into this file. For command receiving and exectuion a [rosbridge server](http://wiki.ros.org/rosbridge_suite) on the Raspberry Pi should be present and running.

