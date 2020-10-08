# -*- coding: utf-8 -*-

import os
import sys

sys.path.append('../')
from pytube import YouTube
from annotator import Annotator


# Set up some folders
demo_folder = r'./'
clips_folder = r'./xxxxxxx'
ourdata_filename = 'xxxxxxx.mp4'

# Create the folders
if not os.path.exists(demo_folder):
    os.mkdir(demo_folder)
if not os.path.exists(clips_folder):
    os.mkdir(clips_folder)

# Initialise the annotator
annotator = Annotator(
    # [
    # {'name': 'clarity 100', 'color': (0, 255, 0)},
    # {'name': 'clarity 80', 'color': (0, 0, 255)},
    # {'name': 'clarity 60', 'color': (0, 255, 255)},
    # {'name': 'clarity 40', 'color': (255, 100, 0)},
    # {'name': 'clarity 20', 'color': (0, 100, 255)}],
    [
    {'name': '1', 'color': (0, 255, 0)},
    {'name': '2', 'color': (0, 0, 255)},
    {'name': '3', 'color': (0, 255, 255)},
    {'name': '4', 'color': (255, 100, 0)},
    {'name': '5', 'color': (0, 100, 255)},
    {'name': '6', 'color': (0, 100, 50)},
    {'name': '7', 'color': (0, 150, 100)},
    {'name': '8', 'color': (50, 100, 255)},
    {'name': '9', 'color': (100, 50, 50)},
    {'name': '10', 'color': (50, 100, 150)},
    {'name': '11', 'color': (100, 100, 200)}
    ],

    clips_folder, sort_files_list=True, N_show_approx=20, screen_ratio=16 / 9,
    image_resize=1, loop_duration=None, annotation_file='ourdata_section.json')

# Split the video into clips
print('Generating clips from the video...')
annotator.video_to_clips(ourdata_filename, clips_folder, clip_length=150, overlap=0, resize=1)

# Run the annotator
annotator.main()