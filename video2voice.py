import ffmpeg
import os, sys
import subprocess

"""
mp4 to flac and judge talk or not by google api
ref: https://www.kinacon-blog.work/entry/2018/10/23/210211
sample: python video2voice.py ./videos/sample.mp4 ./voices/sample.flac
"""

assert len(sys.argv) == 3, "please set video path in argv1 and saving voice path in argv2"
input_file = sys.argv[1]
output_file = sys.argv[2]

cmd = "ffmpeg -y -i {} -vcodec copy -af volume=10dB -ac 1 {}".format(input_file, output_file)
resp = subprocess.check_output(cmd, shell=True)
