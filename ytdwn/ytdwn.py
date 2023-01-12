from assets import functions, yt_functions

TARGET_DIR = "download"

valid_arguments = ["-m", "-h"]
links = []
to_music = False
links, to_music = functions.validate_arguments(valid_arguments)

functions.create_dir(TARGET_DIR)

for link in links:
    try:
        yt_functions.download(link, TARGET_DIR, to_music)
    except Exception as inst:
        print(inst)
        continue
