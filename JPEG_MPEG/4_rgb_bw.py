import subprocess

# FFmpeg installation location
ffmpeg = "/home/josep/bin/ffmpeg"   # CHANGE IT TO YOURS TO TEST

# Getting input image and setting default
input_file = input("Input File (default test.jpg): ")
if input_file == "":
    input_file = "test.jpg"

# Naming output file after input file
output_file = input_file[:-4] + "_bw.jpg"
output_file_compressed = output_file[:-4] + "_compr.jpg"

def build_ffmpeg_command():
    # Adapt user input to fit ffmpeg command
    commands_list_1 = [
        ffmpeg,
        "-i",
        input_file,
        "-vf",
        "format=gray",
        output_file
    ]
    commands_list_2 = [
        ffmpeg,
        "-i",
        output_file,
        "-q:v",
        "31",
        output_file_compressed
    ]

    return [commands_list_1, commands_list_2]

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

# Results comment
# It can be observed that the image size is reduced from 5,7MB to 448kB when
# converted into Black and White. This is a very high compression, probably due
# to ffmpeg automatically compressing by itself. When further compression is
# applied, a minimum of 355kB is achieved. Observing both BW images (compressed
# vs. heavily compressed), a lack of detail can be observed in the heavily
# compressed one.
