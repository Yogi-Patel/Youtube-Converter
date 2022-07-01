import argparse
import os 
 
def default():
	print("Enter a number as per your choice")
	print("1. Download MP3 of video at given URL")
	print("2. Download video from given URL") 
	print("3. Convert from one media format to another ")

	while(True):
		choice = int(input())
		
		if (choice > 0 and choice < 4): 
			break
		else: 
			print("Enter a valid option")

	if (choice == 1):
		URL = input("Enter the URL \n")
		ToMp3(URL)
	elif (choice ==2):
		URL = input("Enter the URL \n")
		Video(URL)
	else: 
		ext = input("Enter the extension of format you want to convert it to (Without a '.') \n")
		filename = input("Enter the filename (w/ extension) which you want to convert \n")
		data_tuple = (ext, filename)
		ffmpeg_convert(data_tuple)

	input("\n\n\n" + "#"*10 + "DONE" + "#"*10)
	os.system("cls")


def ToMp3(URL):
	command = "youtube-dl -o \"C:\\Users\\yogir\\Downloads\\%(title)s.%(ext)s\" -x --audio-format mp3 --audio-quality 256K --embed-thumbnail --add-metadata " + URL
	os.system(command)

def Video(URL):
	command = "youtube-dl -o \"C:\\Users\\yogir\\Downloads\\%(title)s.%(ext)s\" -f bestvideo+bestaudio " + URL
	os.system(command)

def ffmpeg_convert(data_tuple):
	ext = data_tuple[0]
	file = data_tuple[1]
	command = "ffmpeg -i " + file +" " + file.split(".")[0] + "."+ ext  
	print(command)
	os.system(command)
	

# Initialize parser
msg = "A somewhat command-line program (that uses youtube-dl and ffmpeg) to download videos."\
+" youtube-dl and ffmpeg are very flexible but there are a lot of commands and I do not want to go about memorising the arguments."\
+" The intention of the program was to make my life easier and I hope it makes yours easier too."
parser = argparse.ArgumentParser(description = msg)
 
# Adding optional argument
parser.add_argument("-mp3", "--tomp3", type = str, help = "Get mp3 of file on given URL. Passed argument can be a playlist \
	(make sure it is public or unlisted. Not sure if private will work) or a single URL")

parser.add_argument("-video", type = str, help = "Download video(s). Passed argument can be a playlist or a single URL")
parser.add_argument("--ffmpeg", nargs=2, metavar=('ext','file'), help = "Convert a format to another")

 
# Read arguments from command line
args = parser.parse_args()
 
if args.tomp3:
    ToMp3(args.tomp3)
elif args.video:
	Video(args.video)
elif args.ffmpeg:
	ffmpeg_convert(args.ffmpeg)
else: 
	while(True):
		default()

