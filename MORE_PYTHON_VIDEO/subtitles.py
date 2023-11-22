import subprocess

def add_subtitles(ffmpeg, file):
    command = [ffmpeg, "-hide_banner", "-i", file, "-vf", "subtitles=subtitle.srt", file[:-4] + "_subt" + file[-4:]]

    if subprocess.run(command).returncode == 0:
        print("FFmpeg Script Ran Successfully")
    else:
        print("There was an error running your FFmpeg script")
