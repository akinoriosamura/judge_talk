import ffmpeg
import os, sys
import subprocess

"""
mp4 to flac and judge talk or not by google api
ref: https://www.kinacon-blog.work/entry/2018/10/23/210211
sample: python change_video2voice.py ./videos/spider_short.mp4 ./voices/noisy.aac
"""

assert len(sys.argv) == 3, "please set video path in argv1 and saving voice path in argv2"
input_file = sys.argv[1]
output_file = sys.argv[2]

cmd = "ffmpeg -y -i {} -vcodec copy -af volume=10dB {}".format(input_file, output_file)
resp = subprocess.check_output(cmd, shell=True)
