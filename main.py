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

user_id = '67458144000'
 
reels = cl.user_reels(user_id) 
 
for reel in reels: 
    cl.like_reel(reel.pk)