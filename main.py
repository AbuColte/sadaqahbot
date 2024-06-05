from instagrapi import Client
import moviepy.editor as mp
import os

INSTAGRAM_USERNAME = os.environ["INSTAGRAM_USERNAME"]
INSTAGRAM_PW = os.environ["INSTAGRAM_PW"]

cl = Client()
cl.login(INSTAGRAM_USERNAME, INSTAGRAM_PW)

media_path = 'quranvideo.mp4'
with open('hashtags.txt', 'r') as file:
    caption = file.read().replace('\n', '')
    file.close()

cl.video_upload(media_path, caption)
medias = cl.hashtag_medias_recent("dailymuhammadsiddiqmenshawi", 3)

for i, media in enumerate(medias):
    cl.media_like(media.id)
    print(f"liked success")
