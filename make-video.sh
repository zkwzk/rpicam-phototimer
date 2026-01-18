# modify the number behind -r, it's the fps, if 60 means 60 photos make 1 frame for 1 second, let's say you take one photo in every 1 minutes, so 1 hour will take 60 photos which will consist for 1 second video
ffmpeg -r 60 -pattern_type glob -i 'timelapse/**/*.jpg' \
-s 1280x720 -vcodec libx264 timelapse.mp4
