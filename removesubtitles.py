
import os

rootDirectory = "../../../../Volumes/My Passport/tutorials"


for subdir, dirs, files in os.walk(rootDirectory):
    for file in files:
        file_path = os.path.join(subdir, file)
        filename = os.fsdecode(file)
        if filename.endswith(".vtt") or filename.endswith(".srt"):
            print(file_path)
            os.remove(file_path)
        else:
            continue
