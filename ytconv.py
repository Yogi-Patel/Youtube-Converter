import argparse
import os 
 

def ToMp3(URL):
	command = "youtube-dl -o \"D:\\Music\\test\\%(title)s.%(ext)s\" -x --audio-format mp3 --audio-quality 256K --embed-thumbnail --add-metadata " + URL
	os.system(command)

def ToMp4(URL):
	command = "youtube-dl -o \"%(title)s.%(ext)s\" -f best " + URL
	os.system(command)

# Initialize parser
msg = "A somewhat command-line program (that uses youtube-dl and ffmpeg) to download videos."\
+" youtube-dl and ffmpeg are very flexible but there are a lot of commands and I do not want to go about memorising the arguments."\
+" The intention of the program was to make my life easier and I hope it makes yours easier too."
parser = argparse.ArgumentParser(description = msg)
 
# Adding optional argument
parser.add_argument("-mp3", "--tomp3", type = str, help = "Get mp3 of file on given URL. Passed argument can be a playlist \
	(make sure it is public or unlisted. Not sure if private will work) or a single URL")

parser.add_argument("-mp4", "--tomp4", type = str, help = "Download video(s) as mp4. Passed argument can be a playlist or a single URL")


 
# Read arguments from command line
args = parser.parse_args()
 
if args.tomp3:
    ToMp3(args.tomp3)
elif args.tomp4:
	ToMp4(args.tomp4)
