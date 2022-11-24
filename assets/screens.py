def help_instructions():
    print("\nUsage to download from link:")
    print("\tytdwn \"https://www.youtube.com/watch?v=Oxj2fxa\" (video)")
    print("\tytdwn -m \"https://www.youtube.com/watch?v=Oxj2fxa\" (music)")
    
    print("\nUsage to download from list in file:")
    print("\tytdwn \"file.txt\" (video)")
    print("\tytdwn -m \"file.txt\" (music)")

def help_command():
    print("\nUsage to get help:")
    print("\tytdwn -h")
    
def help_screen():
    print("ytdwn - YouTube Downloader\nDownload video (mp4) or music (mp3) from YouTube.")
    help_instructions()

def wrong_parameters():
    print("Error! Wrong parameter(s).")
    help_command()

def resource_missed():
    print("Error! Wrong parameter, link or file missed.")
    help_command()
