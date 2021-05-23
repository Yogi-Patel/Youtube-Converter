import argparse
import os 
 
# Initialize parser
msg = "A somewhat command-line program (that uses youtube-dl and ffmpeg) to download videos."\
+"youtube-dl and ffmpeg are very flexible but there are a lot of commands and I do not want to go about memorising the arguments"\
+"\n The intention of the program was to make my life easier and I hope it makes yours easier too."
parser = argparse.ArgumentParser(description = msg)
 
# Adding optional argument
parser.add_argument("-mp3", "--tomp3",help = "Get mp3 of file on given URL. \n Passed argument can be a text file or a single YouTube URL")
 
# Read arguments from command line
args = parser.parse_args()
 
if args.tomp3:
    print("Diplaying Output as: % s" % args.tomp3)