# Prisec

Anti-spy program for teenagers who want to watch something alone in their room without their parents seeing them. 

## Author

Pooya Shams kolahi

## License

licensed under MIT license. you can use this program as you wish. but please let me know if you have any addition to it.

## Requirements

python 3.x >= 3.6  
opencv-python >= 4.x  
xdotool  
playerctl  
amixer (found in alsa-utils)  

## Usage

this program connects to droidcam application's server for sharing the camera from your mobile phone (you can't use your laptop's webcam to monitor your rooms door. can you?), so you should have the application installed on your mobile phone and run it before running this program. however you won't need to install the client and drivers since prisec uses the web feed to fetch the image every frame.  

for running this program you should have python 3.x and opencv module installed on your computer. for now prisec just runs under linux operating system with the packages `xdotool`, `playerctl` and `alsa-utils` installed. However, I am planning to modify it to work with windows and mac too.

you can install all the above packages using the following commands in ubuntu or other debian based distros (I've tested it on ubuntu)

#### python3

```sh
sudo apt install python3
```

#### xdotool

```sh
sudo apt install xdootool
```

#### alsa-utils

```sh
sudo apt install alsa-utils # this is installed by default on ubuntu
```

#### opencv

```sh
sudo apt install python3-pip # for installing pip which will be used to install opencv
pip3 install --user opencv-python
```

now that you have all the dependencies installed it's time to run the program. open droidcam application on your mobile phone and point your mobile phone camera to your room's door. make sure that both your mobile phone and computer are connected to the same local network. at this part you can run a web client on your browser to check if the app is working fine. you can do this by entering the url provided by droidcam app. it looks like this `http://192.168.x.y:4747/video`. after making sure that the server is working right, change the camera_index variable to the link provided by droidcam + "/mjpegfeed" you can see it in line 11. it should look like this:

```python
camera_index = "http://192.168.x.y:4747/mjpegfeed"
```

you can change the functionality of the program when your door opens by editing the `do_job` function found on line 28.  
since this program uses image diffs to identify moving objects, you might want to change the hyper parameters for sensitivity of the diffs by changing the `lower` and `upper` variables in line 22 and 23 respectively. the smaller the range between the numbers in each array the less sensitive the program is. it's better to keep `upper` as it is with three 255s meaning that the highest change in the image is the highest change possible and change sensitivity by increasing and decreasing the numbers in `lower` array (increasing results in more sensitivity and decreasing results in less sensitivity).
after applying all your configurations to the code you can run it and see if it works by moving something in front of the camera.  
note that the program finishes after doing the job once and if does make sure to run it again.
