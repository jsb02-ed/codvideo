import subprocess

# FFmpeg installation location
ffmpeg = "/home/josep/bin/ffmpeg"   # CHANGE IT TO YOURS TO TEST

def grab_user_input():
    # Function to ask the user and set a default value
    def filter_input(message, default):
        user_input = input(message)
        if user_input == "":
            user_input = default
        return user_input

    print("Hit enter for default values\n")

    # Save user inputs for every parameter in a dictionary
    user_input_dict = {}

    user_input_dict["input_file"] = filter_input("Input File (default test.jpg): ", "test.jpg")
    user_input_dict["frame_size"] = filter_input("Frame Size (default = 320x240): ", "scale=320x240")  # Fix this!!
    user_input_dict["output_file"] = filter_input("Output File (default test_resized.jpg): ", "test_resized.jpg")

    return user_input_dict

def build_ffmpeg_command():
    # Run user parameters selection and save it
    final_user_input = grab_user_input()

    # Adapt user input to fit FFmpeg command
    commands_list = [
        ffmpeg,
        "-i",
        final_user_input["input_file"],
        "-vf",
        final_user_input["frame_size"],
        final_user_input["output_file"]
    ]

    return commands_list

# Check if FFmpeg is running and send the generated command
def run_ffmpeg(commands):
    print(commands)
    if subprocess.run(commands).returncode == 0:
        print("FFmpeg Script Ran Successfully")
    else:
        print("There was an error running your FFmpeg script")

# Call FFmpeg and send the command
run_ffmpeg(build_ffmpeg_command())