# Program Description 

This program uses youtube-dl and ffmpeg to download videos and convert them to formats of your choosing 


# Requirements 

You need to have youtube-dl installed and you should download ffmpeg and add it to your System PATH variable (if you are using Windows)

You can get them at:   
https://www.gyan.dev/ffmpeg/builds/   
https://github.com/yt-dlp/yt-dlp   
(Download recommended .exe for windows and keep it in the same place as FFMPEG which is optional. I did it so that I can have it all in the same PATH in the environment variable)

# Usage 

#### You can use it as a youtube to mp3 converter by running: 
The command that this runs is geared more towards music as it embeds the thumbnail, saves the title and artists.

```
python ytconv.py -mp3 <youtube_url>
```
*The youtube_url can be a playlist or a single video*.
*The mp3 will be downloaded with a bitrate of 256. You can change it by modifying the code. Changing 256 in line 6 to a bitrate of your liking* 
 
I am assuming this works for other sites supported by youtube-dl as well but I have not tried it on my own 



#### Download videos as well: 
```
python ytconv.py -mp4 <URL>
```

This works for all sites supported by youtube-dl 


#### Convert one format to another: 
```
python ytconv.py --ffmpeg <extension of format you want> <file w/ extension which you want to convert> 
```

The `<extension of format you want>` should not contain "**.**" 
For example, if you want to convert to `.mp4`, then pass it as `mp4` only. 

#### Run it without arguments
```
python ytconv.py
```

This gives you a menu-based option. It is fairly intuitive

 
