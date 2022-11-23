import os
import re
import sys
from sys import argv
# from time import sleep

from pytube import YouTube

TARGET = "download"
FILE = "list.txt"

# for i in range(101):
#         sleep(0.01)
#         sys.stdout.write("\r{0}[{1}*{0}]{1} Preparing environment... %d%%".format("GREEN", "END") % i)
#         sys.stdout.flush()
# exit()        

def isUrl(string):
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    return re.match(regex, string)

def on_progress(chunk, file_handle, bytes_remaining):
    global filesize
    current = ((filesize - bytes_remaining)/filesize)
    percent = ('{0:.1f}').format(current*100)
    progress = int(50*current)
    status = '█' * progress + '-' * (50 - progress)
    sys.stdout.write(' ↳ |{bar}| {percent}%\r'.format(bar=status, percent=percent))
    sys.stdout.flush()

if len(argv) == 1:
    print("ytdwn - YouTube Downloader\nDownload video (mp4) or music (mp3) from YouTube.")
    print("\nUsage to download video:")
    print("ytdwn \"https://www.youtube.com/watch?v=Oxj2fxa\"")
    print("\nUsage to download music:")
    print("ytdwn -m \"https://www.youtube.com/watch?v=Oxj2fxa\"")
    
    print("\nUsage to download from list in file:")
    print("ytdwn -l \"file.txt\" (video)")
    print("ytdwn -m -l \"file.txt\" (music)")
    exit(1)

listArguments = argv[1:]
listLinks = []
filesize = 0

toVideo = True
toMusic = False

while ("-l" in listArguments):
    idx = listArguments.index("-l")
    listArguments.pop(idx)

while ("-m" in listArguments):
    idx = listArguments.index("-m")
    listArguments.pop(idx)
    toMusic = True

if toMusic == False:
    toVideo = True
else:
    toVideo = False

if len(listArguments) == 0:
    if os.path.exists(FILE) == False:
        print("Error!: link or file missed.")
        print("\nUsage to download video:")
        print("ytdwn \"https://www.youtube.com/watch?v=Oxj2fxa\"")
        print("\nUsage to download music:")
        print("ytdwn -m \"https://www.youtube.com/watch?v=Oxj2fxa\"")
        
        print("\nUsage to download from list in file:")
        print("ytdwn -l \"file.txt\" (video)")
        print("ytdwn -m -l \"file.txt\" (music)")
        exit(0)
    else:
        listArguments.append(FILE)
    
if isUrl(listArguments[0]) != None:
    listLinks.append(listArguments[0])
else:
    if os.path.exists(listArguments[0]) == False:
        print("Error!: file not exist.")
        print("\nUsage to download video:")
        print("ytdwn \"https://www.youtube.com/watch?v=Oxj2fxa\"")
        print("\nUsage to download music:")
        print("ytdwn -m \"https://www.youtube.com/watch?v=Oxj2fxa\"")
        
        print("\nUsage to download from list in file:")
        print("ytdwn -l \"file.txt\" (video)")
        print("ytdwn -m -l \"file.txt\" (music)")
        exit(0)
        
    with open(listArguments[0]) as f:
        listLinks = f.readlines()

listaux = []
for line in listLinks:
    lineAux = line.strip().replace(" ", "")
    if len(lineAux) > 0:
        listaux.append(line.strip().replace(" ", ""))

listLinks = listaux

exit_while = False
while exit_while == False:
    exit_while = True
    for link in listLinks:
        if (isUrl(link) == None):
            listLinks.remove(link)  
            exit_while = False  

if os.path.exists(TARGET) == False:
    os.mkdir(TARGET)

for link in listLinks:
    try:
        yt = YouTube(link, on_progress)
    except:
        # Exception as inst:
        # print(type(inst))    # the exception instance
        # print(inst.args)     # arguments stored in .args
        # print(inst)          # __str__ allows args to be printed directly,
        #                  # but may be overridden in exception subclasses
        print(f"Error!: {link} is not a link YouTube.")
        continue
    print(f"Try to download \"{link}\", video title \"{yt.title}\"...")

    sys.stdout.write('Connecting with YouTube, wait a moment...')
    sys.stdout.flush()
    if toMusic:
        # extract only audio
        video = yt.streams.filter(only_audio=True).first()
    else:
        video = yt.streams.get_highest_resolution()

    filesize = video.filesize
    sys.stdout.write('\rFileSize : ' + str(round(filesize/(1024*1024))) + 'MB' + (' ' * 30) + '\n')
    sys.stdout.flush()

    # download the file
    out_file = video.download(output_path=TARGET)

    new_file = ""
    # save the file
    base, ext = os.path.splitext(out_file)
    if toMusic:
        new_file = base + '.mp3'
    else:
        new_file = base + '.mp4'
    os.rename(out_file, new_file)

    # result of success
    print(yt.title + " has been successfully downloaded.")
