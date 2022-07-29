# 20-media

## ffmpeg

```ssh
cuda: ffmpeg -codecs | findstr cuvid  
  
transcode: ffmpeg -threads 3 -i *.flv -c copy *.mp4  
merge: ffmpeg -threads 3 -f concat -i list.txt -c copy *.mp4  
split: ffmpeg -threads 3 -ss 00:00:00 -t 00:00:00 -i *.mp4 -codec copy -acodec copy *.mp4  
  
encode: ffmpeg -i *.mp4 -r 60 -vcodec hevc_nvenc -preset slow -ab 192k -ar 44100 -b:v 6000k -maxrate 24400k -minrate 5800k *.mp4  
encode:(additional) -c:v h264_nvenc  
  
music: ffmpeg -i *.mp4 -vn -acodec copy *.aac  
subtitle:ffmpeg -c:v h264_cuvid -i *.mp4 -vf subtitles=*.ass -c:v h264_nvenc -b:v 6000k -c:a copy *.mp4
```