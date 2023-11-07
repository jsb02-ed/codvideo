# PYTHON & VIDEO

In this folder you will find some scripts that modify video calling FFmpeg from Python. Feel free to test them all.

## Before you start...
You must set your own FFmpeg installation location before you run any script that calls FFmpeg. You will find a variable called `ffmpeg` at the beggining of each script needing this change.
Just type something like `ffmpeg = "/home/username/bin/ffmpeg"`

There is a very useful script named `F_run_all.py`. You can just run this one and it will automatically run each other script sequentially.

## Scripts summary

#### 1_mp4_to_mpg.py
This script converts a mp4 video into an mpg video, meaning that it is converting it to MPEG-2. It converts it by calling `FFmpeg`. You can change the input video.

#### 2_modify_resolution.py
The second script changes the resolution of a given video. You can output any resolution as long as it is supported by `FFmpeg`.

#### 3_chroma_subsampling.py
The third script changes the chroma subsampling of a video. Just type `?` when the chroma is asked to see all the available options in `FFmpeg`. You can use them all.

#### 4_video_info.py
The fourth script calls `FFprobe` to output all the available information of a video. `FFprobe` is used instead of `FFmpeg` to avoid giving a `NULL` output.

#### 5_inheritate.py
The fifth script creates a child class `VideoConverter` which inherits from the JPEG_MPEG class: `DCTConverter`. The parent class encodes and decodes a matrix using DCT.

A new method is added to `VideoConverter`. That is `convertVideo(self, file)`. It takes a single frame of a given video to be able to encode/decode it using `DCTConverter`.


#### That's it for today. Now just have fun testing these scripts!