import subprocess

# FFprove installation location
ffprobe = "/home/josep/bin/ffprobe"     # CHANGE IT TO YOURS TO TEST

# Getting input file and setting default
input_file = input("Input File (default BigBuckBunny.mp4): ")
if input_file == "":
    input_file = "BigBuckBunny.mp4"

def build_ffmpeg_command():
    # Adapt user input to fit ffmpeg command
    commands_list = [
        ffprobe,
        "-hide_banner",     # Supress printing copyright notice, build options and library versions
        input_file,
    ]

    return [commands_list]

# Check if ffmpeg is running and send the generated command
def run_ffmpeg(commands):
    for command in commands:
        print(command)
        if subprocess.run(command).returncode == 0:
            print("FFmpeg Script Ran Successfully")
        else:
            print("There was an error running your FFmpeg script")

# Call ffmpeg and send command
run_ffmpeg(build_ffmpeg_command())