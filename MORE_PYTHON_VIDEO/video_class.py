import subprocess
from subtitles import add_subtitles
from histogram import extract_yuv_hist

# FFmpeg installation location
ffmpeg_install = "/home/josep/bin/"  # CHANGE IT TO YOURS TO TEST
ffmpeg = ffmpeg_install + "ffmpeg"
ffprobe = ffmpeg_install + "ffprobe"


class VideoClass:
    cut_file = ""

    def __init__(self, file):
        self.file = file

    def run_ffmpeg(self, command):
        if subprocess.run(command).returncode == 0:
            print("FFmpeg Script Ran Successfully")
        else:
            print("There was an error running your FFmpeg script")

    # PART 1
    def cut_video(self, seconds):
        self.cut_file = self.file[:-4] + f"_cut_{str(seconds)}_sec{self.file[-4:]}"
        command = [ffmpeg, "-hide_banner", "-i", self.file, "-ss", "90", "-t", str(seconds), "-c", "copy", self.cut_file]
        self.run_ffmpeg(command)

    def macro_blocks(self):
        command = [ffmpeg, "-flags2", "+export_mvs", "-i", self.cut_file, "-vf", "codecview=mv=pf+bf+bb",
                   f"{self.cut_file[:-4]}_macroblocks{self.cut_file[-4:]}"]
        self.run_ffmpeg(command)

    # PART 2
    def cut_only_video(self, seconds):
        self.cut_file = self.file[:-4] + f"_cut_{str(seconds)}_sec_mute{self.file[-4:]}"
        command = [ffmpeg, "-i", self.file, "-ss", "90", "-t", str(seconds), "-c", "copy", "-an", self.cut_file]
        self.run_ffmpeg(command)

    def export_audio(self, input_file, output_file, channels=2, bitrate=None, codec=None):
        cmd = [
            'ffmpeg',
            '-i', input_file,
            '-vn',  # Disable video
            '-ac', str(channels),  # Set number of audio channels
        ]
        if bitrate:
            cmd += ['-b:a', bitrate]
        if codec:
            cmd += ['-c:a', codec]
        cmd += [output_file]

        self.run_ffmpeg(cmd)

    def package_mp4(self, video_file, audio_mono, audio_stereo, audio_aac, output_file):
        cmd = [
            'ffmpeg',
            '-i', video_file,
            '-i', audio_mono,
            '-i', audio_stereo,
            '-i', audio_aac,
            '-map', '0', '-map', '1', '-map', '2', '-map', '3',
            '-c:v', 'copy',
            '-c:a', 'copy',
            output_file
        ]
        self.run_ffmpeg(cmd)

    # PART 3
    def count_tracks(self):
        command = ["ffprobe", "-hide_banner", "-show_entries", "stream=channels", "-of", "compact=p=0:nk=1", "-v", "0",
                   self.file]
        result = subprocess.run(command, capture_output=True, text=True)

        if result.returncode == 0:
            # Successful execution, count the tracks
            tracks = result.stdout.strip().split('\n')
            num_tracks = len(tracks)
            print(f"The container contains {num_tracks} tracks.")
            return num_tracks
        else:
            # Error occurred
            print(f"Error counting tracks: {result.stderr}")
            return None


# TESTING CLASS

# Getting input file and setting default
input_file = input("Input File (default BBB.mp4): ")
if input_file == "":
    input_file = "BBB.mp4"

# Selecting part to test
def select_test_part():
    test_part = input("Test Part (1, 2, 3, 4 or 5): ")
    if test_part not in ("1", "2", "3", "4", "5"):
        print("ERROR! Input must be (1, 2, 3, 4 or 5)")
        test_part = select_test_part()
        return test_part
    else:
        return test_part


test_part = select_test_part()
print(f"\n--------------------------------------------")
print(f"             SELECTED TEST: {test_part}")
print(f"--------------------------------------------\n")

# Creating VideoClass variable
video_test = VideoClass(input_file)

# Initiating tests

# PART 1
if test_part == "1":
    video_test.cut_video(9)
    video_test.macro_blocks()  # FIX!

# PART 2
elif test_part == "2":
    # Cut BBB into a 50-second video
    video_test.cut_video(50)
    # Cut BBB into a 50-second video without audio
    video_test.cut_only_video(50)
    # Export BBB(50s) audio as MP3 mono track
    video_test.export_audio("BBB_cut_50_sec.mp4", "audio_mono.mp3", channels=1)
    # Export BBB(50s) audio in MP3 stereo w/ lower bitrate
    video_test.export_audio("BBB_cut_50_sec.mp4", "audio_stereo_low_bitrate.mp3", channels=2, bitrate="64k")
    # Export BBB(50s) audio in AAC codec
    video_test.export_audio("BBB_cut_50_sec.mp4", "audio_aac.aac", codec="aac")
    # Package everything in a .mp4 with FFmpeg
    video_test.package_mp4("BBB_cut_50_sec_mute.mp4", "audio_mono.mp3", "audio_stereo_low_bitrate.mp3",
                           "audio_aac.aac", "BBB_new_package.mp4")

# PART 3
elif test_part == "3":
    video_test.count_tracks()

# PART 4
elif test_part == "4":
    add_subtitles(ffmpeg, input_file)

# PART 5
elif test_part == "5":
    extract_yuv_hist(ffmpeg, input_file)
