import subprocess

# FFmpeg installation location
ffmpeg_install = "/home/josep/bin/"  # CHANGE IT TO YOURS TO TEST
ffmpeg = ffmpeg_install + "ffmpeg"
ffprobe = ffmpeg_install + "ffprobe"
ffplay = ffmpeg_install + "ffplay"

class VideoConverter:

    def run_ffmpeg(self, command):
        if subprocess.run(command).returncode == 0:
            print("FFmpeg Script Ran Successfully")
        else:
            print("There was an error running your FFmpeg script")

    def select_codec(self):
        codec = input("Select codec (VP8, VP9, h265 or AV1): ")
        if codec not in ("VP8", "VP9", "h265", "AV1"):
            print("ERROR! Input must be (VP8, VP9, h265 or AV1)")
            codec = self.select_codec()
            return codec
        else:
            return codec

    def convert_into(self, input, codec):
        if codec == "VP8":
            command = "ffmpeg", "-i", input, "-c:v", "libvpx", "-crf", "10", "-b:v", "1M", "-c:a", "libvorbis", f"{input[:-4]}_{codec}.webm"
            self.run_ffmpeg(command)
        elif codec == "VP9":
            # Two-pass is the recommended encoding method for libvpx-vp9 as some quality-enhancing encoder features are only available in 2-pass mode.
            command = "ffmpeg", "-i", input, "-c:v", "libvpx-vp9", "-crf", "30", "-b:v", "0", f"{input[:-4]}_{codec}.webm"
            self.run_ffmpeg(command)
        elif codec == "h265":
            command = "ffmpeg", "-i", input, "-c:v", "libx265", "-crf", "26", "-preset", "fast", "-c:a", "aac", "-b:a", "128k", f"{input[:-4]}_{codec}.mp4"
            self.run_ffmpeg(command)
        elif codec == "AV1":
            command = "ffmpeg", "-i", input, "-c:v", "libaom-av1", "-crf", "30", f"{input[:-4]}_{codec}.mkv"
            self.run_ffmpeg(command)
    
    def video_comparison(self, left, right):
        command = "ffmpeg", "-i", left, "-i", right, "-filter_complex", "hstack", "video_comparison.mp4"
        self.run_ffmpeg(command)

    def video_comparison_display(self, left, right):
        self.video_comparison(left, right)
        command = "ffplay", "video_comparison.mp4"
        self.run_ffmpeg(command)
