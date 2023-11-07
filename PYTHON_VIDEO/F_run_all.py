import subprocess

# List of Python script exercises
exercises = [
    "1_mp4_to_mpg.py",
    "2_modify_resolution.py",
    "3_chroma_subsampling.py",
    "4_video_info.py",
    "5_inheritate.py",
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