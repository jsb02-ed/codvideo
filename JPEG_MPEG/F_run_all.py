import subprocess

# List of Python script exercises
exercises = [
    "1_rgb_yuv.py",
    "2_ffmpeg_resize.py",
    "3_serpentine.py",
    "4_rgb_bw.py",
    "5_run_length_encoding.py",
    "6_dct_encoder_decoder.py",
]

# Run each Python script one after the other
for script in exercises:
    print(f"\n--------------------------------------------")
    print(f"Running exercise {script} ...")
    print(f"--------------------------------------------\n")
    result = subprocess.run(["python3", script])
    if result.returncode == 0:
        print(f"\n--------------------------------------------")
        print(f"Script {script} executed successfully.")
        print(f"--------------------------------------------\n")
    else:
        print(f"\n--------------------------------------------")
        print(f"Error executing script {script}.")
        print(f"--------------------------------------------\n")

print(f"\n--------------------------------------------")
print(f"             That's all Folks!")
print(f"--------------------------------------------\n")