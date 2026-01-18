import os
import sys
import time
from datetime import datetime
from camera import exposureCalc
from config import config

def try_to_mkdir(path):
    if os.path.exists(path) == False:
        os.makedirs(path)

def prepare_dir(base, now):
    path = str(now.year)
    try_to_mkdir(base + "/" + path)

    return path

def make_os_command(config, exposureMode , file_name):
    height = config["height"]
    width = config["width"]

    os_command = "/usr/bin/rpicam-still "

    os_command = os_command + "--height "+str(height)+\
        " --width "+str(width)+\
        " --output "+file_name
    return os_command

def run_loop(base, pause, config):
    am = config["am"]
    pm = config["pm"]
    exposureCalc1= exposureCalc(am, pm)

    current_milli_time = lambda: int(round(time.time() * 1000))

    print("Pause : " + str(pause))

    while True:
        hoursMinutes = int(time.strftime("%H%M"))
        exposureMode = exposureCalc1.get_exposure(hoursMinutes)
        take_shot = exposureCalc1.take_shot(hoursMinutes)

        if (take_shot == True):
            now = datetime.now()
            path = prepare_dir(base, now)
            name = (
                f"{path}_"
                f"{now.month:02d}_"
                f"{now.day:02d}_"
                f"{now.hour:02d}_"
                f"{now.minute:02d}.jpg"
            )
            print("Capturing " + name + " in " + exposureMode + " mode")
            file_name = base + "/" + path + "/" + name

            os_command = make_os_command(config, exposureMode, file_name)
            os.system(os_command)
            print("Written: " + file_name)
        else:
            print("Shot cancelled during hours of darkness")

        time.sleep(pause)

if(__name__ == '__main__'):
    if len(sys.argv) < 1:
        exit()
    else:
    	try:
            	pauseInterval = int(sys.argv[1])
            	basePath=config["base_path"]
            	run_loop(basePath,pauseInterval, config)
    	except KeyboardInterrupt:
    		print ("Cancelling take.py")
