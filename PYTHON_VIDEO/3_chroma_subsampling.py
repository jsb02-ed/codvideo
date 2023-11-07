import subprocess

# FFmpeg installation location
ffmpeg = "/home/josep/bin/ffmpeg"  # CHANGE IT TO YOURS TO TEST

# Getting input file and setting a default
input_file = input("Input File (default BigBuckBunny_short.mp4): ")
if input_file == "":
    input_file = "BigBuckBunny_short.mp4"

# Choosing new chroma subsampling
def ask_chr_subs():
    chr_subs = input("Choose any chroma subsampling you want. Don't know the codes? Just type ? to see the full list (default = 8-bit 4:2:0): ")
    if chr_subs == "":
        chr_subs = "yuv420p"
    elif chr_subs == "?":
        subprocess.run([ffmpeg, "-pix_fmts"])
        chr_subs = ask_chr_subs()
    return chr_subs

format = "format=" + ask_chr_subs()

# Naming output file after input file
output_file = input_file[:-4] + "_new_chr_subs" + input_file[-4:]

def build_ffmpeg_command():
    # Adapt user input to fit FFmpeg command
    commands_list = [
        ffmpeg,
        "-i",
        input_file,
        "-vf",
        format,
        output_file
    ]
    return [commands_list]

# Check if FFmpeg is running and send the generated command
def run_ffmpeg(commands):
    for command in commands:
        print(command)
        if subprocess.run(command).returncode == 0:
            print("FFmpeg Script Ran Successfully")
        else:
            print("There was an error running your FFmpeg script")

# Call FFmpeg and send command
run_ffmpeg(build_ffmpeg_command())