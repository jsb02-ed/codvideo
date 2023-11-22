import subprocess

def extract_yuv_hist(ffmpeg, file):
    command = [ffmpeg, "-hide_banner", "-i", file, "-vf", "split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay", "-c:v", "libx264", "-c:a", "copy", file[:-4] + "_hist" + file[-4:]]

    if subprocess.run(command).returncode == 0:
        print("FFmpeg Script Ran Successfully")
    else:
        print("There was an error running your FFmpeg script")
