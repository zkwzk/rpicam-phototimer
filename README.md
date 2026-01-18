rpicam-phototimer - create timelapses with your Raspberry Pi with `rpicam-still`
==========
rpicam-phototimer gives you a smart way to capture photos for your timelapses. It is smart because it only takes pictures between the hours you specify and creates a useful folder structure. It is simple because it only depends on Python and `rpicam-still` both of which are normally already available.

Example videos:

How to use
------------------
1. modify the `config.py` to config the sleep time of the camera like the dart time.
This is an example `config.py` file which stop taking photos between 20:00-4:00(+1)
```python
config = {}
config["am"] = 400
config["pm"] = 2000
```


2. it will store the photo in `./timelapse/{year}` folder with the format `YYYY_MM_DD_HH_MM.jpg`, for example `2026_01_18_11_12.jpg`

3. if you are using ssh, better to use screen so it can run in background after you close the ssh connection, you can modify the interval in the start.sh, like 60 for 1minute interval, if less than 60, for now the photo name will conflict since it didn't include the seconds, so it will override the existing file
```
screen
chmod +x start.sh
./start.sh
```
To reconnect later type in `screen -r`.

4. after take the photo, use the `./killscreen` to kill the script
5. use `./make-video.sh` to make a time-lapse video based on the photo it took, it will generate the `timelapse.mp4` under the root folder
