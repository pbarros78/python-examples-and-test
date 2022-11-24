import sys, os, time
from pytube import YouTube

filesize = 0

def on_progress(chunk, file_handle, bytes_remaining):
    filesize = globals()['filesize']
    current = ((filesize - bytes_remaining) / filesize)
    percent = ('{0:.1f}').format(current * 100)
    progress = int(50 * current)
    status = '█' * progress + '-' * (50 - progress)
    sys.stdout.write('\r↳ |{bar}| {percent}%\r'.format(bar=status, percent=percent))
    sys.stdout.flush()

def download(link, target_dir, is_music = False):
    start = time.time()
    try:
        yt = YouTube(link, on_progress)
    except:
        raise Exception(f"Error!: {link} is not a link YouTube.")

    print(f"Try to download \"{link}\"...")

    sys.stdout.write('Connecting with YouTube, wait a moment...')
    sys.stdout.flush()

    if is_music:
        # extract only audio
        video = yt.streams.filter(only_audio=True).first()
    else:
        video = yt.streams.get_highest_resolution()

    filesize = video.filesize
    globals()['filesize'] = filesize
    sys.stdout.write('\r' + (' ' * 50))
    sys.stdout.flush()

    # download the file
    out_file = video.download(output_path=target_dir)

    new_file = ""
    type_file = "Video"
    # save the file
    base, ext = os.path.splitext(out_file)
    if is_music:
        new_file = base + '.mp3'
        type_file = "Music"
    else:
        new_file = base + '.mp4'
    os.rename(out_file, new_file)

    # result of success
    sys.stdout.write(f"\rYouTube video \"{yt.title}\" {' ' * 30}\n")
    sys.stdout.flush()
    print(f"File: {new_file} ({type_file})\nSize: {str(round(filesize/(1024*1024), 2))} MB\nDownload duration: {round(time.time() - start, 2)} seconds\nHas been successfully downloaded.")
