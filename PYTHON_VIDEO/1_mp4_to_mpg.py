import subprocess

# FFmpeg installation location
ffmpeg = "/home/josep/bin/ffmpeg"   # CHANGE IT TO YOURS TO TEST

# Getting input file and setting default
input_file = input("Input File (default BigBuckBunny_short.mp4): ")
if input_file == "":
    input_file = "BigBuckBunny_short.mp4"

# Naming output file after input file
output_file = input_file[:-4] + "_converted.mpg"

def build_ffmpeg_command():
    # Adapt user input to fit ffmpeg command
    commands_list = [
        ffmpeg,
        "-i",
        input_file,
        output_file
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