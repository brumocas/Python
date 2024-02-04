from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print("Title:", yt.title)

print("Views:", yt.views)

yd = yt.streams.get_highest_resolution()

output_path = ""

yd.download(output_path = output_path)