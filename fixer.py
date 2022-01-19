import os
import glob
import re
from mutagen.oggvorbis import OggVorbis    # for editing OGG metadata

def oggfix():
    smpathlist = i.split(os.sep)
    sm_path = smpathlist[0:len(smpathlist)-1]
    path = "\\".join(sm_path) + "\\"
    for j in glob.glob(glob.escape(path) + "*.ogg"):
        print(j)
        tags = OggVorbis(j)    # read current OGG file tags
        if 'title' not in tags:    # if missing title tag
            tags['title'] = titleLine
            tags.save()
            print("Title tag added to " + re.split('\\\\', j)[-1])
        if 'artist' not in tags:   # if missing artist tag
            tags['artist'] = artistLine
            tags.save()
            print("Artist tag added to " + re.split('\\\\', j)[-1])

def main():
    path = input("Enter the directory of the files to fix.")
    path = path.replace(os.sep, "\\")      # replace forward slashes
    path = os.path.join(path, '')       # add trailing slash if it is not there
    global i
    for i in glob.glob(glob.escape(path) + "**/*.sm", recursive=True):  # loop through all SM files in script folder or subdirectories
        global artistLine, titleLine
        artistLine = titleLine = ""
        with open(i, 'r') as smfile:    # read SM file and close when done
            lines = smfile.readlines()
            for line in lines:  # iterate through lines
                if re.search(r'TITLE', line):   # matches first occurrence of string
                    titleLine = re.split(';|:', line)[1]
                    break
            for line in lines:
                if re.search(r'ARTIST', line):
                    artistLine = re.split(';|:', line)[1]
                    break
        oggfix()

main()